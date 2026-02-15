names = set()

while True:
    name = input("Enter a name:").strip()
    if name == "":
        break

    if name in names:
        print("This name is already taken.")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)
