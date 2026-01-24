gender = input("Enter the biological gender: ")
value = int(input("Enter the hemoglobin value: "))

if gender == "female":
    if 117 <= value <= 155:
        print("normal")
    elif value < 117:
        print("low")
    else:
        print("high")
elif gender == "male":
    if 117 <= value <= 155:
        print("normal")
    elif value < 117:
        print("low")
    else:
        print("high")

