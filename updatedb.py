"""
Update Database

This script allows the user to connect to a database and return the version
This is a baseline that will be adapted to have update capability, in conjunction with 
code to update the necessary rows based on what has changed
"""
import click
import psycopg2
import pandas as pd
from date_attribute_functions import last_sat_pass, last_wet_obs


@click.command()
@click.option("--database", default="waterbodies", help="Database to connect to")
def updatedb(database):
    """
    Connect to the provided database and retrieve version information
    """

    try:
        # Create a connection to the database
        connection = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432",
            database=database,
        )

        # Create a cursor, which will perform data base operations
        cursor = connection.cursor()

        # Get all ids from database
        cursor.execute(
            """
            SELECT DISTINCT uid, timeseries
            FROM dea_waterbodies
        """
        )

        record = cursor.fetchall()

        # Update rows for each record in the table
        for uid_value, csv_value in record:
            df = pd.read_csv(csv_value)

            dt_satpass_value = last_sat_pass(df)
            dt_wetobs_value = last_wet_obs(df)

            dt_satpass_sql = """
                UPDATE dea_waterbodies
                SET dt_satpass = %s,
                    dt_wetobs = %s
                WHERE uid=%s;
            """
            cursor.execute(
                dt_satpass_sql,
                (
                    dt_satpass_value,
                    dt_wetobs_value,
                    uid_value,
                ),
            )

            # Execute the database transactions
            connection.commit()

    # Should the connection fail, display an error message
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    # At the end, if a connection was establsihed, close the cursor and connection
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    updatedb()
