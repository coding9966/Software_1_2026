import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="metropolia",
        password="metropolia",
        database="test"
    )
    cursor = connection.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code.upper(),))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return (result[0], result[1])
    else:
        return None

def main():
    icao1 = input("Enter the ICAO code of the first airport: ").strip()
    icao2 = input("Enter the ICAO code of the second airport: ").strip()
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)
    if not coords1:
        print(f"No airport found with ICAO code '{icao1.upper()}'")
        return
    if not coords2:
        print(f"No airport found with ICAO code '{icao2.upper()}'")
        return
    distance_km = geodesic(coords1, coords2).kilometers
    print(f"The distance between {icao1.upper()} and {icao2.upper()} is {distance_km:.2f} km.")

if __name__ == "__main__":
    main()