"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Jack Kang 
Email: Yanjun.Kang@metropolia.fi
Date: 21.1.2026
Assignment: https://github.com/metropolia-sw/python/blob/main/en/Exercises.md#4-while-loops-while
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random

#Task 4.1
i = 1
while i < 1000 :
    if i % 3 == 0:
        print(i)
    i += 1


#Task 4.2
while True:
    inches = float(input("Please input the number of inches (Negative to quite): "))
    if inches < 0 :
        break
    centimeters = inches * 2.54
    print(centimeters)


#Task 4.3
numbers = []
while True:
    user_input = input("Please input the number: ")

    if user_input == "":
        break
    numbers.append(float(user_input))

    if numbers:
        print("the minimum number is ", min(numbers))
        print("the maximum number is ", max(numbers))
    else:
        print("there are no numbers")


#Task 4.4
random_number = random.randint(1, 10)
guess_number = -1
while guess_number != random_number:
    guess = int(input("Please input the guess: "))
    if guess == random_number:
        print("Correct")
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")
        

#Task 4.5
username = "Metropolia"
password = "abc"
input_username = ""
input_password = ""
input_count = 0
while username != input_username or password != input_password:
    input_username = input("Please input the username: ")
    input_password = input("Please input the password: ")
    input_count += 1
    if username == input_username and password == input_password:
        print("Welcome")
        break
    if input_count > 5:
        print("Access denied")
        break


#Task 4.6
random_points = int(input("Please enter the the random points you wanted: "))
inside_circle = 0

for _ in range(random_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1

pi = 4 * inside_circle / random_points
print("pi= ", pi)
