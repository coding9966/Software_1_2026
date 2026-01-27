number = int(input("Enter a number: "))

prime = False

for i in range(2, int(number**0.5)+1):
    if number % i == 0:
        prime = True

print("the number " + str(number) + " is prime: " + str(prime))