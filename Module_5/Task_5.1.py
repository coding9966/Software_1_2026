import random

sum = 0

dice_number = int(input("Enter the dice number: "))

for i in range(1, dice_number + 1):
    roll = random.randint(1, 6)
    sum += roll

print(sum)