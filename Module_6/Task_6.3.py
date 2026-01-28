def gallons_to_liters(gallons):
    return gallons * 3.785

def main():
    while True:
        gallons = float(input("Enter the gallons: "))

        if gallons < 0:
            print("The gallons is negative, end!")

        liters = gallons_to_liters(gallons)
        print(f"{liters:.2f} liters")

main()