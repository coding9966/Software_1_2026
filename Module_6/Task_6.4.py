
def creat_list():
    numbers = []
    while True:
        input_number = int(input("Enter a number: "))
        if input_number < 0:
            return numbers
        else:
            numbers.append(input_number)


def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def main():
    numbers = creat_list()
    print("The sum is: ", sum_list(numbers))

main()