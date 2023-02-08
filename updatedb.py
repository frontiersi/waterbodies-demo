import click
import psycopg2


@click.command()
@click.option("--database", default="waterbodies", help="Database to connect to")
def updatedb(database):
    """
    Connect to the provided database and retrieve version information
    """

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432",
            database=database,
        )

        cursor = connection.cursor()

        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")

        cursor.execute("SELECT version();")

        record = cursor.fetchone()
        print(f"You are connected to {record} \n")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    updatedb()
