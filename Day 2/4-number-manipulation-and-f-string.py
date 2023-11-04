print(22 / 7)
print(type(22 / 7))
print(int(22 / 7))

# Round numbers
print(round(22 / 7))
print(round(22 / 7, 4)) # Precision
print("{:.4f}".format(22 / 7))

# Floor division
print(22 // 7)
print(type(22 // 7))

# Manipulate value
result = 22 / 7
result /= 7
print(result)

score = 0
score += 1
print(score)

# F-string conversion
# print("Your score is " + score)
# TypeError: can only concatenate str (not "int") to str

print(f"Your score is {score} and your result is {result}")