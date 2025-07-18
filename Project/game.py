import random

signs = ["rock", "paper", "scissors"]

player1 = str(
    input(" Player 1: Enter the move you want to throw(rock,paper,scissors):"))

# Python has a built-in module that you can use to make random numbers.
# choice() is an inbuilt function that returns a random item from a list, tuple, or string.
# We have to import random to use choice() method.
computer = random.choice(signs)
print("Computer selects: ", computer)

if (player1 == computer):
    print("Draw")
elif (player1 == "rock" and computer == "scissors"):
    print("Player1 Won.", "computer Lost.")
elif (player1 == "rock" and computer == "paper"):
    print("computer Won.", "Player1 Lost")
elif (player1 == "paper" and computer == "rock"):
    print("Player1 Won.", "computer Lost.")
elif (player1 == "paper" and computer == "scissors"):
    print("computer Won.", "Player1 Lost")
elif (player1 == "scissors" and computer == "rock"):
    print("computer Won.", "Player1 lost.")
elif (player1 == "scissors" and computer == "paper"):
    print("computer Won.", "Player1 Lost.")
else:
    print("You have entered wrong move.")
