# habitatSuitability
Habitat Suitability

See
[Habitat Suitability #603](https://github.com/earthlab-education/Earth-Analytics-AY24/issues/603).

Need [DOI](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/)

## [Our changing climate is changing where key grassland species can live, and grassland management and restoration practices will need to take this into account.](https://www.frontiersin.org/articles/10.3389/fpls.2017.00730/full)

In this project, you will create a habitat suitability model for _Sorghastrum nutans_ (or a plant species of your choice), a grass native to North America. [In the past 50 years, its range has moved northward](https://www.gbif.org/species/2704414). The model will be based on combining multiple data layers related to soil, topography, and climate. You will also demonstrate the coding skills covered in this class by creating a modular, reproducible workflow for the model.

Due 15 Dec. Some useful links:

- [Habitat Suitability Coding Challenges](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/notebooks/08-habitat/habitat.html)
- [Final Projects 2023](https://github.com/earthlab-education/Earth-Analytics-2023-01-Intro/blob/main/analysis/final.md)
- [Subtract Rasters in Python](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/raster-data-processing/subtract-rasters-in-python/)
- Working Examples in 2024
    - [Ed Chan](https://github.com/eggvoice/sorghastrum-nutans-habitat-suitability-model)
    - [Hannah Rieder](https://github.com/hanried/habitat-suitability) &
[doc 00](https://github.com/hanried/habitat-suitability/blob/main/00-habitat-suitability.ipynb)
    - [Alison Post](https://github.com/akpost21/Habitat-Suitability) &
[akpost21.github.io](https://github.com/akpost21/akpost21.github.io)
    - [Christopher Quinn](https://github.com/cmq879/earth-analytics-habitat-suitability-finalproject)
- Videos
    - [POLARIS Soil Intro](https://cuboulder.zoom.us/rec/play/E2GIn3h6mY9Z7BaaxCDAape0mCD-gQhaBCplqp7T0FbFLCbZbVNXAOUS8jloBH4PvB__6bsQwR-xLkoe.S5-dDjshYndL1Mib?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fcuboulder.zoom.us%2Frec%2Fshare%2FimhCGJcrCgSoE1cJjg02r86GMNjiRz0jwVMJ5c0uWNwBCD5D_0kLSl3CaqLdDI2a.ucGta1EEAiirDUop)
    - [POLARIS Soil Multiple Tiles](https://cuboulder.zoom.us/rec/play/V_jdL5O3ePUCkAlt__yYG2tOIM8cI8BBI61z4114Awf3lVPBD_XaO_kUSOCCCBlqeq4XCsdkWuvivYCl.JpFRlK-EbErBsiay?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fcuboulder.zoom.us%2Frec%2Fshare%2F3S7pGOSv7jztZTvg4RSXLj-GicnHwusIDIEDoETZbUN7ivkc6Ryi5GAJyX9Ly6h2.VXl6iFmLChjjUyOg)
    - [MACA THREDDS Climate Projections](https://o365coloradoedu-my.sharepoint.com/personal/alpo6007_colorado_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Falpo6007%5Fcolorado%5Fedu%2FDocuments%2FAttachments%2FGMT20241204%2D184128%5FRecording%5F1758x1024%201%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E9d3173e0%2D79c8%2D4027%2D95d3%2D7b49bec923d0)
    - [Shuttle Radar Topology Mission (SRTM)](https://cuboulder.zoom.us/rec/play/6fTikKcJPbGPB321iHmAa3dhMUR7r0n_zSZ3XxjL-SfBLpVfsrZJ1CrHlkOrK6jvTlYgztvvskfvaAGP.T6ixGvWj42gYShMV?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fcuboulder.zoom.us%2Frec%2Fshare%2FploG3HVb_qA0QU8eACIHMKtNbkiGFys7cmiBbTRryv3NUWBmKo-DXhzXdU3cbpz7.99x0PeiCHONSj6Ty)
    - [Harmonizing](https://cuboulder.zoom.us/rec/play/ekGBLwpW4gdtvlBstJrS_ehlAzq9INvK37XNdS8WKF-3WfE2xTiZmn1xIlFysuymN67yGbUeUJlpAwzS.HPT5luF6NWi8Ylsl?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fcuboulder.zoom.us%2Frec%2Fshare%2FgtkCgeowtvOgVPHDddcElI144wxCyHXOj1lKi5SEiMlxY1-L9Zm-PDBuTe6lh3Gm.S4X4wzflnTKXQtqr)
    - [Zenodo DOI](https://www.canva.com/design/DAGZAYa4S9g/EMFly0i8e9YDDFL4QuEMaQ/watch?utm_content=DAGZAYa4S9g&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h7cebe8067b)
## You will create a reproducible scientific workflow

Your workflow should:

1. **Define your study area:**  If you are using Sorghastrum nutans, you can download from the
[USFS National Grasslands](https://www.fs.usda.gov/managing-land/national-forests-grasslands/national-grasslands)
via the
[Units ZIPfile](https://data.fs.usda.gov/geodata/edw/edw_resources/shp/S_USA.NationalGrassland.zip) and select **at least 2** as study sites.

- Resources:
    - Duan, K., Sun, G., Sun, S. et al. Divergence of ecosystem services in U.S. National Forests and Grasslands under a changing climate. Sci Rep 6, 24441 (2016). [DOI: 10.1038/srep24441](https://doi.org/10.1038/srep24441)
    - [USFS Maps](https://www.fs.usda.gov/visit/maps)
        - [USFS ArcGIS Grassland Units](https://data-usfs.hub.arcgis.com/datasets/usfs::national-grassland-units-feature-layer/explore?location=41.300146%2C-107.829591%2C6.23)
        - [USFS IVM Digital Map](https://www.fs.usda.gov/ivm/)
        - [Download PDF or JPG Map](https://experience.arcgis.com/experience/9ab8d03e2bec4d7fbfc27ba836e70aed/page/Forest-Series/#data_s=id%3AdataSource_2-Forest_Series_Index_6205%3A1430)
    - [ArcGIS Map Viewer](https://www.arcgis.com/home/webmap/viewer.html)
    - Great resource for plant growth characteristics: <https://plants.usda.gov/>
- Yandell Proposed Study Sites:
    - [Buffalo Gap National Grassland](https://www.fs.usda.gov/recarea/nebraska/recarea/?recid=30329)
[Recreation Area](https://www.fs.usda.gov/detail/r2/recreation?cid=stelprdb5389082)
[Data Download](https://data-usfs.hub.arcgis.com/datasets/usfs::national-grassland-units-feature-layer/explore?location=43.534637%2C-102.565490%2C8.34)
(OBJECTID 186937, NATIONALGRASSLANDID 295518010328)	
    - [Oglala National Grassland](https://www.fs.usda.gov/recarea/nebraska/recarea/?recid=30328)
[Visit](https://visitnebraska.com/harrison/oglala-national-grassland)
[Data Download](https://data-usfs.hub.arcgis.com/datasets/usfs::national-grassland-units-feature-layer/explore?location=43.509639%2C-102.570535%2C8.36)
(OBJECTID 186940, NATIONALGRASSLANDID 295521010328)
   
2. **Fit a model:** For each grassland:
    1. **Download model variables** as raster layers covering your study area envelope, including:
        - At least one **soil** variable from the [POLARIS dataset](http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/) (**find thresholds**)
            - <https://scholars.duke.edu/publication/1381493>
            - <https://gee-community-catalog.org/projects/polaris/>
        - Elevation from the SRTM (available from the [earthaccess API](https://github.com/nsidc/earthaccess/))
            - this is the hardest one to work with! 
        - At least one **climate** variable from the [MACAv2 THREDDS data server](http://thredds.northwestknowledge.net:8080/thredds/reacch_climate_CMIP5_macav2_catalog2.html).
            - Compare **two climate scenarios** of your choice (e.g. different time periods, different emission scenarios) 
            - [GeoNetwork: Harvesting THREDDS](https://docs.geonetwork-opensource.org/3.12/user-guide/harvesting/harvesting-thredds/)
            - [EDA Lesson 2. Intro to CMIP and MACA v2 Climate Data](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/intro-to-MACAv2-cmip5-data/)
            - [CMIP5 GCMs Ensemble Models](https://climate.northwestknowledge.net/MACA/GCMs.php)
            - Has different CRS, so have to project these data. May need `netCDF4` library, maybe `seaborn`.
            - Variables: air temp, precip, rel hum?
            - [try and except error catching python](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/get-maca-2-climate-data-netcdf-python/)
        - [NASA Earth Observation Data](https://earthdata.nasa.gov/)
        - [Community Earth System Models (CESM)](https://www.cesm.ucar.edu)
     2. **Calculate at least one derived **topographic** variable** (slope or aspect) to use in your model. You probably will wish to use the `xarray-spatial` library, which is available in the latest earth-analytics-python environment (but will need to be installed/updated if you are working on your own machine). Note that calculated slope may not be correct if you are using a CRS with units of *degrees*; you should re-project into a projected coordinate system with units of *meters*, such as the appropriate UTM Zone.
     3. **Harmonize your data** - make sure that the grids for each of your layers match up. Check out the [`ds.rio.reproject_match()` method](https://corteva.github.io/rioxarray/stable/examples/reproject_match.html#Reproject-Match) from `rioxarray`.
     4. **Build your model**. You can use any model you wish, so long as you explain your choice. However, if you are not sure what to do, we recommend building a **fuzzy logic** model (see below).
3. **Present your results** in at least one figure for each grassland/climate scenario combination.
   - project site
   - model
   - assumptions
   - findings
   - visualization
   - [Zenodo DOI](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/) **get account on Zenodo**

## If you are unsure about which model to use, we recommend using a fuzzy logic model

To train a fuzzy logic habitat suitability model:

1. Research S. nutans, and find out what optimal values are for each variable you are using (e.g. soil pH, slope, and current climatological annual precipitation). 
2. For each **digital number** in each raster, assign a value from 0 to 1 for how close that grid square is to the optimum range (1=optimal, 0=incompatible). 
3. Combine your layers by multiplying them together. This will give you a **single suitability number** for each square. Check out this [article about raster math](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/raster-data-processing/subtract-rasters-in-python/) for more info.
4. Optionally, you may apply a threshold to make the most suitable areas pop on your map.

## You will be evaluated on your code AND how you present your results

I will use the following rubric:

| Description | Maximum Points |
| - | - |
| **GITHUB REPOSITORY** | 30  |
| Project is stored on GitHub | 3 |
| The repository has a README that introduces the project | 5 |
| The README also explains how to run the code | 5 |
| The README has a DOI badge at the top | 5 |
| The repository has a LICENSE | 2 |
| Repository is organized and there are not multiple versions of the same file in the repository | 5 |
| Repository files have machine and human-readable names | 5 |
| **CODE** | 120 |
| The code runs all the way through using the instructions from the README | 10 |
| The code follows the PEP-8 style standard | 10 |
| The code is well-documented with comments | 10 |
| The code uses functions and/or loops to be DRY and modular | 10 |
| Any functions have numpy-style docstrings | 10 |
| The code makes use of conditionals to cache data and/or computations, making efficient use of computing resources | 10 |
| The code contains a site map for the US National Grassland(s) used (1 ugrad, 2+ grad) | 10 |
| For each grassland (ugrad 1, grad 2+), the code downloads at least model variables as raster layers: soil, elevation, and climate (ugrad 1, grad 2 scenarios) | 10 |
| The code correctly calculates a derived topographic variable | 10 |
| The code harmonizes the raster data | 10 |
| For each climate scenario (1 ugrad, 2+ grad), the code builds a habitat suitability model | 10 |
| For each grassland/climate scenario combination, the code produces at least one (sub)figure displaying the results | 10 |
| Any unfinished components have detailed pseudocode or a flow diagram **explaining** how they could be finished in the future, and or a **complete** bug report explaining the problem | *up to 90 points, in place of other categories* |
| **WRITTEN ANALYSIS** | 50 |
| The notebook contains a project description | 10 |
| The notebook contains a researched site description | 10 |
| The notebook contains a data description and citation for each data source | 10 |
| The notebook contains a model description | 10 |
| The notebook contains a headline and description for each figure | 10 |
