import random

class Board:

    def __init__(self):
        self.size = 6
        self.board = [[' '] * self.size for _ in range(5)]

    def print_board(self, is_computer_board=False):

        print(' ', ' '.join(str(i) for i in range(1, self.size + 1)))
        for i in range(5):
            row = [' ' if cell == 'B' and is_computer_board else cell for cell in self.board[i]]
            print(i+1, ' '.join(row))

class Player:

    def __init__(self, name):
        """
        Represents a player in the game.
        using the string name set the player's name.
        using the player name set the score's for this player. 
        """
        self.name = name
        self.score = 0

    def get_player_name(self):
        name = input("Enter your name: ")
        self.player = Player(name)
    

class BattleshipGame:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()

    def welcome_message(self):
        """
        Displays a welcome message to the players.
        """
        print("Welcome to Guess Battleship Game!")
        print("All you have to do is find the computer's boats and sink them.")
        print("Follow the instructions and good luck.")
        print()

    def get_player_name(self): 
        """
        Gets the player's name and creates a Player object.
        """
        name = input("Enter your name: ")
        self.player = Player(name)


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
    
    def start_game(self):
        self.welcome_message()
        self.get_player_name()

        # Place ships on the boards
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

        # Print the boards
        self.print_boards()


game = BattleshipGame()

# Start the game
game.start_game()


game = BattleshipGame()

# Place ships on the boards
game.place_ships(game.player_board)
game.place_ships(game.computer_board)

# Print the boards
game.print_boards()


#shots from the player 

#shots from the computer 

#ships remaining

#end game 
