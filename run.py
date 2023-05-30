import random

#battleship game

# welcome game 

print("Welcome to Guess Battleship Game!")
print("All you have to do is find the computers boat and sinks them")
print("Follow the instructions and good luck.")
    
#insert matrices 

player = []
computer = []
computer_hidden= []

#display the game board for player and computer 
for x in range(4):
    player.append(["O"] * 6)
for y in range(4):
    computer.append(["O"] * 6)
for z in range(4):
    computer_hidden.append(["O"] * 6)

print(player)
print(computer)
print(computer_hidden)

class Board:

    def __init__(self):
        self.size = 6
        self.board = [[' '] * self.size for _ in range(5)]

    def print_board(self, is_computer_board=False):

        print(' ', ' '.join(str(i) for i in range(1, self.size + 1)))
        for i in range(5):
            row = [' ' if cell == '' and is_computer_board else cell for cell in self.board[i]]
            print(i + 1, ' '.join(row))

class BattleshipGame:

    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()

    def place_ships(self, board):

        for _ in range(4):
            while True:
                row = random.randint(0, 4)
                col = random.randint(0, 5)
                if board.board[row][col] == ' ':
                    board.board[row][col] = 'B'
                    break

    def print_boards(self):

        print("Computer's board:")
        self.computer_board.print_board(is_computer_board=True)

        print("\nPlayer's board:")
        self.player_board.print_board()

# Create an instance of the BattleshipGame class
game = BattleshipGame()

# Place ships on the boards
game.place_ships(game.player_board)
game.place_ships(game.computer_board)

# Print the boards
game.print_boards()

#get the players name and show in the init message

#shots from the player 

#shots from the computer 

#ships remaining

#end game 


