# Input variable
name = input("What is your name? ")
print(name)

name = "Ahmad"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)