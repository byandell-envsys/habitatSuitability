def soil_url_dict(place_gdf, soil_var="sand", soil_sum="mean", soil_depth="100_200"):
    """
    Set up soil URLs based on place.
    
    Parameters
    ----------
        place_gdf: GeoDataFrame
            GeoDataFrame of selected location
        soil_var, soil_sum, soil_depth: character string
            Name of soil variable, summary and depth

    Results
    -------
        soil_url: dict
            Dictionary of URLs
    """
    from math import floor, ceil
    
    soil_url_template = (
        "http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/"
        f"{soil_var}/"
        f"{soil_sum}/"
        f"{soil_depth}/"
        "lat{min_lat}{max_lat}_lon{min_lon}{max_lon}.tif")
    
    # soil_url_template.format(min_lat = 43, max_lat = 44, min_lon = -103, max_lon = -104)

    bounds_min_lon, bounds_min_lat, bounds_max_lon, bounds_max_lat = (place_gdf.total_bounds)

    # Initialize structure for saving image links
    url_names = []
    for min_lon in range(floor(bounds_min_lon), ceil(bounds_max_lon)):
        for min_lat in range(floor(bounds_min_lat), ceil(bounds_max_lat)):
            url_names.append(f"lon{min_lon}lat{min_lat}")

    soil_urls = {url_name: [] for url_name in url_names}
    for min_lon in range(floor(bounds_min_lon), ceil(bounds_max_lon)):
        for min_lat in range(floor(bounds_min_lat), ceil(bounds_max_lat)):
            print(min_lon, min_lat)
            soil_url = soil_url_template.format(min_lat = min_lat, max_lat = min_lat + 1,
                min_lon = min_lon, max_lon = min_lon + 1)
            soil_urls[f"lon{min_lon}lat{min_lat}"].append(soil_url)

    return soil_urls

# soil_urls = soil_url_dict(place_gdf, soil_var="sand", soil_sum="mean", soil_depth="100-200")

def merge_soil(soil_urls):
    """
    Merge soil data.
    """
    import geopandas as gpd
    import rioxarray as rxr
    from rioxarray.merge import merge_arrays # Merge rasters
    
    #soil_das = {url_name: [] for url_name in list(soil_urls.keys())}
    soil_das = []
    for soil_key in list(soil_urls.keys()):
        soil_url = soil_urls[soil_key][0]
        print(soil_key)
        soil_da = rxr.open_rasterio(soil_url, mask_and_scale=True).squeeze()

        # Store the resulting DataArray for later
        soil_das.append(soil_da)

    print('Done.')

    # Merge all tiles
    soil_merged_das = merge_arrays(soil_das) 

    return soil_merged_das

# soil_merged_das = merge_soil(soil_urls)

def process_maca(sites, scenarios=['pr'], climates=['rcp85', 'rcp45'], years = [2026]):
    """
    Process MACA Monthly Data.

    Parameters
    ----------
    sites: dict of GeoDataFrames
       dictionary with GeoDataFrames
    scenarios: character string
        'pr' = precipitation
    climates: character string
        'rcp' = relative concentration pathway
    years: numeric
        first year of 5-year period

    Returns
    -------
    maca_df: DataFrame
        data frame with parameters and values
    """
    import rioxarray as rxr
    import xarray as xr
    import pandas as pd
    import geopandas as gpd
    
    def convert_lonlat(longitude):
        return ((longitude + 180) % 360) - 180
    
    maca_da_list = []
    for site_name, site_gdf in sites.items():
        for scenario in scenarios:
            for year in years:
                for climate in climates:
                    year_end = year + 4
                    maca_url = (
                        "http://thredds.northwestknowledge.net:8080/"
                        "thredds/dodsC/MACAV2/BNU-ESM/"
                        "macav2metdata_"
                        f"{scenario}_BNU-ESM_r1i1p1_{climate}"
                        f"_{year}_{year_end}_CONUS_monthly.nc")
                    print(maca_url)
                    # Read data and set up coordinates.
                    maca_da = xr.open_dataset(maca_url).squeeze().precipitation
                    maca_da = maca_da.assign_coords(
                        lon = ("lon", [convert_lonlat(l) for l in maca_da.lon.values]),
                        lat = ("lat", [convert_lonlat(l) for l in maca_da.lat.values]))
                    maca_da = maca_da.rio.set_spatial_dims(x_dim='lon', y_dim='lat')
                    # Clip bounds.
                    bounds = site_gdf.to_crs(maca_da.rio.crs).total_bounds
                    maca_da = maca_da.rio.clip_box(*bounds)
                    maca_da_list.append(dict(
                        site_name = site_name,
                        scenario = scenario,
                        year = year,
                        climate = climate,
                        da = maca_da))
    return pd.DataFrame(maca_da_list)

# maca_df = process_maca({'buffalo': buffalo_gdf}, ['pr'], ['rcp85', 'rcp45'], [2026])