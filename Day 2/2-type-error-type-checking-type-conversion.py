num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")
# Error due to str + int + str

# type checking
print(type(num_char))

# type conversion: int(), str(), float()
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")