# Text-based Adventure Game:Develop a simple text-based adventure game with multiple choices for the player.
# Input values:
# Player makes choices by selecting options presented in the game.
# Output value:
# Story progression based on player choices, with different outcomes.
# Example:
# Input values:
# 1. Enter the dark cave.
# 2. Follow the path through the forest.
# Output value:
# You chose to enter the dark cave. Inside, you find a treasure chest.
# Input values:
# 1. Open the chest.
# 2. Leave the cave.
# Output value:
# You chose to open the chest. Congratulations! You found a valuable gem.

option1 = "Enter the dark cave."
option2 = "Follow the path through the forest."
print(f"1. {option1}")
print(f"2. {option2}")

user_input = int(input("Select Option( 1 or 2): "))

if user_input == 1:
    print("You chose to enter the dark cave, You find the treasure chest.")
    option3 = "Open the chest."
    option4 = "Leave the cave"
    print(f"3. {option3}")
    print(f"4. {option4}")
    next_input = int(input("Select Option(3 or 4): "))       
    if next_input == 3:
        print("You chose to open the chest.")
        print("Congratulations! You find a valuable gem.")
    elif next_input == 4:
        print("You leaved the cave.")
        print("You lost.")  
elif user_input == 2:
    print("Follow the path through the forest.")
    print("You have been killed by the wild animals.")
else:
    print("Invalid Move.")