import mysql.connector

def get_airport_by_icao(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="metropolia",
        password="metropolia",
        database="test"
    )

    cursor = connection.cursor()

    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code.upper(),))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def main():
    icao_code = input("Enter the ICAO code of the airport: ").strip()
    airport = get_airport_by_icao(icao_code)

    if airport:
        name, town = airport
        print(f"Airport Name: {name}")
        print(f"Location (Town): {town}")
    else:
        print("No airport found with that ICAO code.")


if __name__ == "__main__":
    main()
