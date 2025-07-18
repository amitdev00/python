# We have used dictionary values to store the values
d = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

# Function to display rows in a grid
def display_row(d, row_number):
    print("     |       |       ")
    print(" ", d[1 + 3 * (row_number - 1)], "  ", "| ", d[2 + 3 * (row_number - 1)], "  ", "|  ", d[3 + 3 * (row_number - 1)], sep='')
    print("     |       |       ")

# Function for printing the horizontal separation between the rows
def display_horizontal_line(n):
    print("=" * n)

# Function for printing the tic-tac-toe grid
def display_board(d):
    for i in range(1, 4):
        display_row(d, i)
        if i < 3:
            display_horizontal_line(17)

# This function takes input for player names and symbols
def player_name():
    user_1 = input("Hi! Please enter the name of the first player: ")
    print("Hi!", user_1)
    user_1_char = input("Please choose your character (x or o): ")

    while user_1_char not in ['x', 'o']:
        print("Looks like you have not entered a valid character.")
        user_1_char = input("Please choose your character (x or o): ")

    user_2 = input("Hi! Please enter the name of the second player: ")
    user_2_char = 'o' if user_1_char == 'x' else 'x'

    print(user_1, "chose", user_1_char)
    print(user_2, "chose", user_2_char)
    return (user_1, user_1_char), (user_2, user_2_char)

# Check if all positions in a particular row are the same
def row_check(d, char, i):
    return d[1 + (i * 3)] == char and d[2 + (i * 3)] == char and d[3 + (i * 3)] == char

# Check if all positions in a particular column are the same
def column_check(d, char, i):
    return d[i + 1] == char and d[i + 4] == char and d[i + 7] == char

# Check if all positions in a particular diagonal are the same
def diag1_check(d, char):
    return d[1] == char and d[5] == char and d[9] == char

def diag2_check(d, char):
    return d[3] == char and d[5] == char and d[7] == char

# This function returns whether a player wins or not after their move
def won(d, char):
    for i in range(3):
        if row_check(d, char, i) or column_check(d, char, i):
            return True
    return diag1_check(d, char) or diag2_check(d, char)

# Check if the board is completely filled
def complete(d):
    return all(d[i] != '' for i in range(1, 10))

# Start the game
(user_1, user_1_char), (user_2, user_2_char) = player_name()

# How numbers are connected to grid
ref = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
print("\nFollowing are number relations to grid cells:")
display_board(ref)

# First chance is default assigned to player 1
player = 1

# Main game loop
while True:
    if player == 1:
        print(f"{user_1}, please select a cell from 1 to 9 where you want to put '{user_1_char}'")
        place = input()
    else:
        print(f"{user_2}, please select a cell from 1 to 9 where you want to put '{user_2_char}'")
        place = input()

    if place not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("You have not chosen from 1 to 9. Please choose from 1-9.")
        continue

    place = int(place)
    if d[place] != '':
        print("This place is already occupied. Try again.")
        continue

    d[place] = user_1_char if player == 1 else user_2_char
    display_board(d)

    if won(d, user_1_char if player == 1 else user_2_char):
        print(f"Congrats! {user_1 if player == 1 else user_2}, You Won!")
        break

    if complete(d):
        print("It's a draw!")
        break

    player = 2 if player == 1 else 1