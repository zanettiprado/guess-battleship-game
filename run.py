import random

class Board:
    """
    Represents the game board.
    it shows the size of the board.
    and the board The 2D list representing the board.
    """

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


    def get_guess(self):
        while True:
            col = input("Guess the column (1-6): ")
            row = input("Guess the row (1-5): ")

            if self.is_valid_input(col, 6) and self.is_valid_input(row, 5):
                col = int(col) - 1
                row = int(row) - 1
                return row, col
            else:
                print("Invalid input. Try again.")

    @staticmethod
    def is_valid_input(value, max_value):
        try:
            value = int(value)
            return 1 <= value <= max_value
        except ValueError:
            return False

class BattleshipGame:
    def __init__(self):
        self.player = None
        self.computer = Player("Computer")
        self.player_board = Board()
        self.computer_board = Board()


    def welcome_message(self):
        """
        Displays a welcome message to the players.
        """
        print("Welcome to Guess Battleship Game!")
        print("All you have to do is find the computer's boats and sink them.")
        print("Follow the instructions and good luck!")
        print()

    def get_player_name(self): 
        """
        Gets the player's name and creates a Player object.
        """
        name = input("Enter your name: ")
        self.player = Player(name)


    def place_ships(self, board):
        """
        Places the battleships on the board.
        """
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

    def get_guess(self, is_player_turn):
        """
        Gets the player's or computer's guess.
        """
        if is_player_turn:
            return self.player.get_guess()
        else:
            while True:
                row = random.randint(0, 4)
                col = random.randint(0, 5)
                if self.computer_board.board[row][col] != 'X':
                    if self.computer_board.board[row][col] == 'B':
                        self.computer_board.board[row][col] = '*'
                        print("The computer hit one of your battleships!")
                        self.player.score += 1
                    else:
                        self.computer_board.board[row][col] = 'X'
                        print("The computer missed your battleships.")
                    return row, col
                        
    def start_game(self):
        """ 
        Place ships on the boards and Print the boards
        Using While Get the guess Check if the guess hits or misses a ship and Switch turns
        
        """
        self.welcome_message()
        self.get_player_name()

        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

        self.print_boards()

        is_player_turn = True
        while True:
            if is_player_turn:
                print(f"\n{self.player.name}'s turn:")
            else:
                print("\nComputer's turn:")

            row, col = self.get_guess(is_player_turn)
            
            if is_player_turn:
                if self.computer_board.board[row][col] == 'B':
                    print("Hit!")
                    self.player.score += 1
                else:
                    print("Miss!")
            else:
                if self.player_board.board[row][col] == 'B':
                    print("The computer sank one of your battleships!")
                else:
                    print("The computer missed its guess.")

            is_player_turn = not is_player_turn

            if self.player.score == 4:
                print(f"\nCongratulations, {self.player.name}! You won!")
                break
            elif self.player.score > 2:
                print("You are getting close!")

            self.print_boards()

game = BattleshipGame()

# Start the game
game.start_game()

# Place ships on the boards

# Print the boards


#shots from the player 

#shots from the computer 

#ships remaining

#end game 
