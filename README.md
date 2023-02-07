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
10. Open a terminal window and type `echo "export GEOSERVER_HOME=/usr/local/geoserver" >> ~/.profile`, then press Enter
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

### Step 3: Install DBeaver (Optional)
1. Navigate to the [DBeaver Download page](https://dbeaver.io/download/)
2. Select the appropriate MacOS .dmg file (Check which chip you have by clicking the Apple icon in your main menu bar and selecting "About this Mac", then look for the "Chip" entry)
3. Open the .dmg file and move the DBeaver icon to the Applications folder
