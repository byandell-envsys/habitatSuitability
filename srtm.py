def srtm(data_dir):
    """
    Download SRTM data using earthaccess API.

    Good elevation map at 30M for slope (0-1) and aspect (0-350).
    """
    import os
    import pathlib
    from glob import glob
    import geopandas as gpd
    import earthaccess
    import rioxarray as rxr
    import xrspatial

    elevation_dir = os.path.join(data_dir, 'srtm')  
    os.makedirs(elevation_dir, exist_ok=True)

    # Use a bounding box
    project_gdf = gpd.read_file(os.path.join(data_dir, 'project_file', 'project_boundary', 'project.shp'))
    project_gdf.plot()

    # Earthaccess API and datasets
    earthaccess.login() 
    datasets = earthaccess.search_datasets(keyword='SRTM DEM')  

    for dataset in datasets:
        print(dataset['umm']['ShortName'], dataset['umm']['EntryTitle'])  
        # Choose SRTMGL1 (1-arc second or ~30m) ## USE THIS

    # Create a tuple based on your bounding box and the SRTM data
    srtm_pattern = os.path.join(elevation_dir, '*.hgt.zip')  

    # Add logic. Files are zipped.
    if not glob(srtm_pattern):
        bounds = tuple(denver_gdf.total_bounds)  
        srtm_results = earthaccess.search_data(short_name='SRTMGL1', bounding_box=bounds)  
        srtm_results = earthaccess.download(srtm_results, elevation_dir)  

    # Process the downloaded SRTM files
    for srtm_file in glob(srtm_pattern):
        print(f"Processing file: {srtm_file}")
        # Add logic to process SRTM files (unzipping, reading, etc)

    return srtm_pattern

