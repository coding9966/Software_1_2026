airports = {}

def enter_new_airport():
    icao = input("Enter the ICAO code of the airport: ").upper()
    if icao in airports:
        print(f"Airport with ICAO code {icao} already exists: {airports[icao]}")
    else:
        name = input("Enter the name of the airport: ")
        airports[icao] = name
        print(f"Airport {name} with ICAO code {icao} added successfully!")

def fetch_airport_info():
    icao = input("Enter the ICAO code of the airport to fetch: ").upper()
    if icao in airports:
        print(f"Airport ICAO code {icao}: {airports[icao]}")
    else:
        print(f"Airport {icao} not found!")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        choice = int(input("Enter your choice(1/2/3): "))

        if choice == 1:
            enter_new_airport()
        elif choice == 2:
            fetch_airport_info()
        elif choice == 3:
            print("Exiting program. Bye for now!")
            break
        else:
            print("Invalid choice! Please enter 1/2/3.")

main()
