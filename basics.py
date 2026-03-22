while True:
    name = input("Enter your name: ")
    try:
        int(name)
        print("Invalid Name.")
    except ValueError:
        break

while True:
    color = input("Enter your favorite color:")

    try:
        int(color)
        print("Invalid Color. Try again")
    except ValueError:
        break

while True:
    try:
        birth_year = int(input("Enter your Birthyear: "))
        if birth_year <= 2026:
            break
        else:
            print("Birthyear must be not above 2026.")

    except ValueError:
        print("Invalid Year. Try Again.")
age = 2026 - birth_year
print("Hello", name)
print("You are", age, "years old")
print("Your favorite color is", color)
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
