import math

def unit_price(diameter, price):
    return price / ((diameter /100 / 2) ** 2 * math.pi)

first_diameter = int(input("Enter the first diameter: "))
first_price = int(input("Enter the first price: "))
second_diameter = int(input("Enter the second diameter: "))
second_price = int(input("Enter the second price: "))

first_unit_price = unit_price(first_diameter, first_price)
second_unit_price = unit_price(second_diameter, second_price)

if first_unit_price < second_unit_price:
    print("The first pizza has a lower price!")
else:
    print("The second pizza has a lower price!")


