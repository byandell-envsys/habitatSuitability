def soil_urls(place_gdf, soil_var="sand", soil_sum="mean", soil_depth="100_200"):
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
        soil_url_list: list of character strings
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

    soil_url_list = []
    for min_lon in range(floor(bounds_min_lon), ceil(bounds_max_lon)):
        for min_lat in range(floor(bounds_min_lat), ceil(bounds_max_lat)):
            print(min_lon, min_lat)
            soil_url = soil_url_template.format(min_lat = min_lat, max_lat = min_lat + 1,
                min_lon = min_lon, max_lon = min_lon + 1)
            soil_url_list.append(soil_url)

    return soil_url_list

# soil_url_list = soil_urls(place_gdf, soil_var="sand", soil_sum="mean", soil_depth="100-200")