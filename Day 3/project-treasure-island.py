print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# decision = input("Left or Right?\n")
# if decision == "Left":
#     decision = input("Swim or Wait?\n")
#     if decision == "Wait":
#         decision = input("Red, Yellow or Blue?\n")
#         if decision == "Yellow":
#             print("You Win!")
#         else:
#             print("Game Over.")
#     else:
#         print("Game Over.")
# else:
#     print("Game Over.")

decision = input("Left or Right?\n")
if decision == "Right":
    print("Game Over.")
    exit()
decision = input("Swim or Wait?\n")
if decision == "Swim":
    print("Game Over.")
    exit()
decision = input("Red, Yellow or Blue?\n")
if decision == "Red" or decision == "Blue":
    print("Game Over.")
    exit()
else:
    print("You Win!")