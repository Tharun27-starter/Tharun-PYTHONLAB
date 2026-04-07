
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

current_year = 2026

age = current_year - year_of_birth


if age >= 60:
    print(name, "is a Senior Citizen.")
else:
    print(name, "is not a Senior Citizen.")