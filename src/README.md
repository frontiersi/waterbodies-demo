# Overview of key scripts

## `src/updatedb.py`

Takes the following command line arguments:

* `--user`: Server username; default=`postgres`
* `--password`: Server pasword; default=`""`
* `--host`: Server host; default=`localhost`
* `--port`: Server port; default=`5432`
* `--database`: Database to connect to; default=`waterbodies`

The database must contain the following columns:

* `uid`
* `area_m2`
* `timeseries`
* `dt_satpass`
* `dt_wetobs`
* `wet_sa_m2`
* `dt_updated`

Run using `python src/updatedb.py --user <user> --password <password> --host <host> --port <port> --database <database>`

This script connects to the existing database, reads the csv stored in the `timeseries` column for each entry, calculates the new attributes, and commits their values to the database.

## `src/attribute_functions.py`

Contains the functions used by `src/updatedb.py`:

* `last_sat_pass`: responsible for calculating new values for `dt_satpass`
* `last_wet_obs`: responsible for calculating new values for `dt_wetobs`
* `last_wet_area`: responsible for calculating new values for `wet_sa_m2`

Each function takes a Pandas dataframe (loaded from the timeseries csv in `src/updatedb.py`).

## `src/longestline.py` 

This script was developed during the project, but is no longer actively used. By design, it would be run to update the database once, and the database would need to have the following columns:
* `longestl`: a well-known-text (WKT) string of the longest line geometry for the polygon
* `longestl_m` : the length of the longest line geometry in metres

> NOTE: The database connection settings are hard-coded in this script. They could be updated to match the `src/updatedb.py` script if desired.