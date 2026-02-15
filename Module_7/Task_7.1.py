#seasons = {'Winter', 'Spring', 'Summer', 'Autumn'}
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

month = int(input("Enter the month: "))

if 1 <= month <=12:
    index = (month % 12) // 3
    print(seasons[index])
else:
    print("Invalid Month")