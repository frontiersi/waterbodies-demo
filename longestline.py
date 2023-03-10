"""
Update the database with longest line

This script allows the user to connect to a database, and update the values
for longestl and longestl_m
"""
import click
import psycopg2


@click.command()
@click.option("--database", default="waterbodies", help="Database to connect to")
def updatedb(database):
    """
    Connect to the provided database. Calculate the longest line
    (using minimum bounding circle method from postGIS) and
    the length of that line. Update corresponding attributes
    in the selected table
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

        # Calculate the longest line and store as a WKT string in longestl
        longestl_sql = """
            UPDATE dea_waterbodies
            SET longestl=ST_AsText(ST_LongestLine(geom, geom));
        """
        cursor.execute(longestl_sql)

        # Calculate the length of longestl and store in longestl_m
        longestlm_sql = """
            UPDATE dea_waterbodies
            SET longestl_m=ST_Length(longestl);
        """
        cursor.execute(longestlm_sql)

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
            print("Operation complete. PostgreSQL connection closed")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    updatedb()
