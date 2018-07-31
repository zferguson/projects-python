# Import random module
from random import randint

# Set variables, lists
board = []
board_size = 5
turns = 10

# Iterate over empty list to create grid
for x in range(0, board_size):
  board.append(["O"] * board_size)

# Edit board to remove punctuation
def print_board(board):
  for row in board:
    print(" ".join(row))

player_name = input("What is your name? ")

# Prints welcome message
# ----------------------
## TBD:
###  - Set welcome message as variable
###  - Include player's name
###  - Allow player to opt in to game or opt out, which returns player to the welcome message

print("Welcome to my first ever coding project, %s!") % (player_name)
print("")
print("You'll recognize this as the classic game of Battleship,")
print("with just a slight change... no actual ships!")
print("But no worries, we can still play, so let's get to it!")
print("")
print("Here is the playing field:")
print("")

print_board(board)

# Set location of "battleship"
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)

# Print location of battleship
print(ship_row)
print(ship_col)

# Everything from here on should be in your for loop
# Don't forget to properly indent!

# Keeps track of what turn it is
for turn in range(turns):
  print("\n--- Turn", turn + 1, " of ", turns, " ---\n")
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

# Determines if input has hit or missed, then returns results
  if guess_row == ship_row and guess_col == ship_col:
    print("\nCongratulations! You sank my battleship!\n")
    break
  else:
    if guess_row not in range(board_size) or \
      guess_col not in range(board_size):
      print("\nOops, that's not even in the ocean.\n")
    elif board[guess_row][guess_col] == "X":
      print("\nYou guessed that one already.\n")
    else:
      print("\nYou missed my battleship!\n")
      board[guess_row][guess_col] = "X"
    if (turn == turns - 1):
      print("Game Over :-(\n")
    print_board(board)