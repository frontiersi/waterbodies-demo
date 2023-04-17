# Addition of new attributes to waterbodies product

## Description
Prototype workflow for enhancing the features of the DEA waterbodies product.

## Overview of key scripts

This repository uses two python files:

* `src/updatedb.py`
* `src/attribute_functions.py`

The first can be run from the command line to update the database. The second contains the utility functions that are used to calculate new attributes. For more information see the [src directory](src/README.md).

## Implementing the workflow for existing Postgres server and GeoServer

### Step 1: Create a spatial database
1. Start your postgres server
2. Create a new database called `waterbodies`
3. Run `CREATE EXTENSION postgis;` to enable postgis for the `waterbodies` database

### Step 2: Add the shapefile to the spatial database
1. Open your terminal and navigate to this repository
2. Create the conda environment for this repository by running `conda env create -f environment.yml` in your terminal
3. Activate the conda environement by running `conda activate waterbodies`
4. To add the sample waterbodies shapefile as a table in the database, run the following command, replacing `<username>` with your username, and `<port>` with the database port

```
ogr2ogr -nln dea_waterbodies -nlt PROMOTE_TO_MULTI -lco GEOMETRY_NAME=geom -lco FID=fid -lco PRECISION=NO -mapFieldType Date=DateTime Pg:"dbname=waterbodies host=localhost user=<username> port=<port>" data/waterbodies_sample.shp -overwrite
```

> NOTE: `-mapFieldType Date=DateTime` is required to convert from the shapefile's Date type to a time-zone aware DateTime in the database.

### Step 3: Launch GeoServer and add the Database
1. Launch the GeoServer and log in
2. Create a workspace
3. Add a new "PostGIS - PostGIS Database" store
4. Publish the store

### Step 4: Update the database
1. Ensure the server is on
2. Activate the conda environement by running `conda activate waterbodies`
3. Calculate and commit the new attributes by running `python src/updatedb.py --database waterbodies`

> NOTE: This currently runs on all waterbodies in the database, and is not configured to run on a per waterbody basis.

## Implementing the workflow locally
Complete instructions for a local install on MacOS are provided in the [workflow directory](workflow/README.md).