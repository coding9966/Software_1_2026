import mysql.connector
from collections import Counter

def get_airports_by_country(country_code):
    """
    Fetch airport types for a given country from the database.
    Returns a list of airport types.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="flight_game"
    )

    cursor = connection.cursor()

    # Query airport types for the given country
    query = "SELECT type FROM airport WHERE iso_country = %s"
    cursor.execute(query, (country_code.upper(),))

    airport_types = [row[0] for row in cursor.fetchall()]  # extract all types

    cursor.close()
    connection.close()

    return airport_types

def main():
    country_code = input("Enter the country code (e.g., FI): ").strip()
    airport_types = get_airports_by_country(country_code)

    if airport_types:
        counts = Counter(airport_types)  # Count airports by type
        print(f"Airports in {country_code.upper()}:")
        # Sort by airport type alphabetically
        for airport_type in sorted(counts):
            print(f"- {counts[airport_type]} {airport_type} airports")
    else:
        print(f"No airports found for country code '{country_code.upper()}'.")

if __name__ == "__main__":
    main()