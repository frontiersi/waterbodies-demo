# waterbodies-demo
Prototype workflow for enhancing the features of the DEA waterbodies product for use by Australian aerial firefighting agencies.

## Set up
This workflow is currently only designed to run locally on Mac OS devices.

### Step 1: Install GeoServer
1. Navigate to the [GeoServer Download page](http://geoserver.org/download)
2. Click the "Stable" release
3. Under Packages, click the "Platform Independent Binary"
4. Wait for the .zip file to download
5. Extract the .zip file in your Downloads folder
6. In a new Finder window, and click "Go" from the main menu bar, then click "Go to Folder..."
7. Type in `/usr/local` and press Enter
8. Create a new folder called `geoserver` - you will need to provide your password
9. Copy and paste the contents of the .zip folder into your new `geoserver` folder
10. Enable CORS by following the [GeoServer Instructions](https://docs.geoserver.org/latest/en/user/production/container.html#enable-cors). Uncomment the `<filter>` for Jetty and the `<filter-mapping>` tags from the `webapps/geoserver/WEB-INF/web.xml` file.
11. Open a terminal window and type `echo "export GEOSERVER_HOME=/usr/local/geoserver" >> ~/.profile`, then press Enter
12. Close the terminal window

### Step 2: Install Postgres.app
1. Navigate to [Postgres.app Download page](https://postgresapp.com/downloads.html)
2. Download the "Latest Release"
3. Open the .dmg file and move the Postgres.app icon to the Applications folder
4. Open the Postgres application (from Applications folder or the Launchpad)
5. Click "Initialize" to create a new server
6. Open a terminal window and type `sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`
7. Close the terminal window

### Step 3: Install DBeaver
1. Navigate to the [DBeaver Download page](https://dbeaver.io/download/)
2. Select the appropriate MacOS .dmg file (Check which chip you have by clicking the Apple icon in your main menu bar and selecting "About this Mac", then look for the "Chip" entry)
3. Open the .dmg file and move the DBeaver icon to the Applications folder

### Step 4: Create a spatial database
1. Open Postgres.app and start the server
2. Open DBeaver and click the "New Database Connection" icon (first icon on the top left of the application window)
3. Select PostgreSQL and click "Next"
4. Leave all settings as they are and click "Finish". You should see a new entry in the navigator labled "postgres - localhost:5432"
5. Click on the postgres entry to reveal the "Databases" item
6. Right-click on the "Databases" item and click "Create New Database"
7. Type `waterbodies` as the Database name and leave all other settings as they are. Click "OK"
8. Right-click the "waterbodies" entry under "Databases" and go to "SQL Editor" then "Open SQL Script"
9. Type `CREATE EXTENSION postgis;` and press the play button (or Control+Enter on the keyboard)
10. Replace the above by typing `SELECT postgis_full_version();` and press the play button (or Control+Enter on the keyboard). You should see a results table appear.

### Step 5: Add a shapefile to the spatial database
1. Open your terminal and navigate to this repository
2. Create the conda environment for this repository by running `conda env create -f environment.yml` in your terminal
3. Activate the conda environement by running `conda activate waterbodies`
4. To add the sample waterbodies shapefile as a table in the database, run the following command, replacing `<username>` with your username (this appears just before the `$` in the terminal e.g. `waterbodies-demo janedoe$`)

```
ogr2ogr -nln dea_waterbodies -nlt PROMOTE_TO_MULTI -lco GEOMETRY_NAME=geom -lco FID=fid -lco PRECISION=NO Pg:"dbname=waterbodies host=localhost user=caitlinadams port=5432" data/waterbodies_sample.shp -overwrite
```

5. In DBeaver, click the "waterbodies" database, then "Schemas" then "public" then "Tables". You should now see "dea_waterbodies" as an entry under "Tables"
6. Double click the "dea_waterbodies" entry to open it in the viewing panel. Click "Data" to see the entries

### Step 6: Launch GeoServer and add the Database
1. Open your terminal and enter `cd /usr/local/geoserver/bin/`
2. Enter `sh startup.sh` to start the GeoServer
3. In your web browser, enter `http://localhost:8080/geoserver`
4. At the top of the page, log in by using the username `admin` and the password `geoserver`
5. On the left-hand side of the interface, clikc "Workspaces"(appears under the "Data" heading)
6. Click "Add new workspace" (green plus icon)
7. Type `waterbodes` in the "Name" field, and type `http://localhost:8080/geoserver/waterbodies` in the "Namespace URI" field
8. Click "Save"
9. On the left-hand side of the interface, click "Stores" (appears under the "Data" heading)
10. Click "Add new Store" (green plus icon)
11. Click "PostGIS - PostGIS Database" (under "Vector Data Sources")
12. Using the dropdown menu, select "waterbodes" as the "Workspace"
12. Type `dea_waterbodies` in the "Data Source Name" field
13. Type `Subsample of DEA Waterbodies` in the "Description" field
14. Type `waterbodies` in the "database" field
15. Type your username in the "user" field - use the same username as action 4 in step 5 
16. Leave all other fields as they are and click "Save"
17. Click "Publish" next to the "dea_waterbodies" in the Layers list that appears 
18. Under "Bounding Boxes" click "Compute from data", then "Compute from native bounds"
19. Click "Apply"
20. At the top of the page, click the "Publishing" tab
21. Under WMS Settings, set the "Default Style" to "polygon"
22. Click "Save"

 You should then be able to see the dea_waterbodies in the Layers list

 ### Step 7: View the WFS on DEA Maps
 1. Open [DEA Maps](https://maps.dea.ga.gov.au/)
 2. Click "Explore Map Data"
 3. Click "My Data"
 4. Click "Add Web Data"
 5. Select "Web Feature Service (WFS) Server" from the drop down list for Step 1
 6. Type `http://localhost:8080/geoserver/waterbodies/ows` in for Step 2
 7. Click "Add"
 8. Click the "GeoServer Web Feature Service" menu
 9. Press the plus icon next to "dea_waterbodies" 
 10. Click "Done"
 11. Click the "Share/Print" button in the top left and save the URL somewhere for future access. This will save you from needing to repeat the above steps. The link will only work on your local machine if all the required services (i.e. Postgres and GeoServer) are running

## Compute longest line
To calculate the longest line (and its length), perform the following

1. Open Postgres and start the server
2. Open DBeaver and ensure you have the `waterbodies` database, containing the `dea_waterbodies` table, and that the table contains the `longestl` and `longestl_m` columns
3. Open your terminal and navigate to this repository
4. Activate the conda environement by running `conda activate waterbodies`
5. Run the `longestline.py` script using
```
python longestline.py
```
6. Open the `dea_waterbodies` table in DBeaver and check that the `longestl` and `longestl_m` columns contain values