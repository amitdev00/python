import random

dice_output = ["1", "2", "3", "4", "5", "6"]

dice1 = random.choice(dice_output)
dice2 = random.choice(dice_output)

sum_dice = (int(dice1) + int(dice2))

Player = int(input("Guess the sum of number  of two dice: "))

print("The number comes in Dice1 is: ", dice1)
print("The number comes in Dice2 is:", dice2)
print("You have entered: ", Player)

if (Player == sum_dice):
    print(f"{sum_dice} is the right guess.")

else:
    print("You are wrong.")
    print("Try Again.")





