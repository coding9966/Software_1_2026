import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides: "))

while True:
    result = roll_dice(sides)
    print("The result is: ", result)
    if result == sides:
        break

