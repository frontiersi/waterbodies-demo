"""
Update Database

This script allows the user to connect to a database and return the version
This is a baseline that will be adapted to have update capability, in conjunction with 
code to update the necessary rows based on what has changed
"""
import click
import psycopg2


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

        # Display connection information
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")

        # Create a cursor, which will perform data base operations
        cursor = connection.cursor()

        # Select the version from the database
        cursor.execute("SELECT version();")

        # Return the information held by the cursor and display
        record = cursor.fetchone()
        print(f"You are connected to {record} \n")

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
