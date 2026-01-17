"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Jack Kang 
Email: Yanjun.Kang@metropolia.fi
Date: 17.1.2026
Function: This programme is the answer of task 2 assignment
https://github.com/metropolia-sw/python/blob/main/en/Exercises.md#2-variables-and-interactive-programs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import random


#Task 2.1
name = input("Enter your name: ")
print("Hello," + name + "!")


#Task2.2
radius = float(input("Enter the radius: "))
area = radius * radius * math.pi;
print("the area is: ", area)


#Task 2.3
rectangle_length = int(input("Enter the length of the rectangle: "))
rectangle_width = int(input("Enter the width of the rectangle: "))
print("the perimeter is: ", (rectangle_length + rectangle_width) * 2)
print("the area is: ", rectangle_length * rectangle_width)


#Task 2.4
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
print("the sum is: ", number_1 + number_2 + number_3)
print("the product is: ", number_1 * number_2 *number_3)
print("the average is: ", (number_1 + number_2 + number_3) / 3)


#Task 2.5
TALENT_TO_POUNDS = 20
POUND_TO_LOTS = 32
LOT_TO_GRAMS = 13.3

talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

total_grams = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS * LOT_TO_GRAMS
         + pounds * POUND_TO_LOTS * LOT_TO_GRAMS
         + lots * LOT_TO_GRAMS)

kilos = int(total_grams // 1000)
grams = total_grams % 1000

print(f"The weight in modern units: \n{kilos} kilograms and {grams:.2f} grams.")


#Task 2.6
code_3 = ""
for _ in range(3):
    code_3 += str(random.randint(0, 9))

code_4 = ""
for _ in range(4):
    code_4 += str(random.randint(1, 6))

print("3-digit radom code: ", code_3)
print("4-digit radom code: ", code_4)
