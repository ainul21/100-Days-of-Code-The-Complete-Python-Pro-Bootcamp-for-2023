# Operators
# and
# or
# not

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are RM 5.")
        bill = 5
    elif 12 < age < 18:
        print("Youth tickets are RM 10.")
        bill = 10
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("Adult tickets are RM 15.")
        bill = 15

    photo = input("Do you want photo? Y or N: ")
    if photo == "Y":
        bill += 3
    print(f"Your total bill is RM{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
