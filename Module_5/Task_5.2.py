nums = []

while True:
    input_num = input("Enter a number: ")

    if input_num == "":
        break
    nums.append(int(input_num))

nums.sort(reverse=True)

for i in nums[:5]:
    print(i)