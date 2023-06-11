import random


class Board:
    """
    Represents the game board.
    Shows the size of the board.
    and the board The 2D list representing the board.
    """

    def __init__(self):
        self.size = 6
        self.board = [[' '] * self.size for _ in range(5)]

    def print_board(self, is_computer_board=False):
        """
        Prints the current state of the board.
        """
        print('-' * (self.size * 2 + 1))
        print(' ', ' '.join(str(i) for i in range(1, self.size + 1)))
        for i in range(5):
            row = [
                ' ' if cell == 'B' and is_computer_board else cell
                for cell in self.board[i]
            ]
            row_string = ' '.join(row)
            print(i + 1, row_string)


class Player:
    """
    Represents a player in the game.
    Using the string name set the player's name.
    Using the player name set the score's for this player.
    """

    def __init__(self, name):
        self.guesses = set()
        self.name = name
        self.score = 0

    class InvalidInputError(Exception):
        pass

    def get_guess(self):
        while True:
            col = input("Guess the column (1-6):\n")
            row = input("Guess the row (1-5):\n")

            if col == '9' or row == '9':
                return None, None

            try:
                col = int(col)
                row = int(row)
                is_col_valid = self.is_valid_input(col, 6)
                is_row_valid = self.is_valid_input(row, 5)

                if not is_col_valid or not is_row_valid:
                    raise self.InvalidInputError

                col -= 1
                row -= 1

                if (row, col) in self.guesses:
                    print("You can't try the same coordinate more than once.")
                    continue

                self.guesses.add((row, col))
                return row, col

            except ValueError:
                print("Invalid input. Try again.")
            except self.InvalidInputError:
                print("Invalid input. Guess out of range. Try again.")

    @staticmethod
    def is_valid_input(value, max_value):
        try:
            value = int(value)
            return 1 <= value <= max_value
        except ValueError:
            return False


class BattleshipGame:
    """
    Represents the Battleship game.
    The main class in the code shows the welcome message and get players name.
    Method to place the boats randomly and start the battle ship game
    The last function will finish the game get all metrics.
    """

    def __init__(self):
        self.player = None
        self.computer = Player("COMPUTER")
        self.player_board = Board()
        self.computer_board = Board()

    def welcome_message(self):
        """
        Displays a welcome message to the players.
        """
        border = ("-" * 50)
        message = "|  Welcome to the Guess Battleship Game!         |\n" \
                  "|  All you have to do is find the computer's     |\n" \
                  "|  boats and sink them. Follow the instructions  |\n" \
                  "|  and good luck. Insert 9 as a guess to abort   |\n" \
                  "|  the game anytime. (number of boats: 4)        |"
        print(border)
        print(message)
        print(border)
        print()

    def get_player_name(self):
        """
        Gets the player's name and creates a Player object.
        """
        name = input("Enter your name:\n")
        self.player = Player(name.upper())

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
        print("COMPUTER's board:")
        self.computer_board.print_board(is_computer_board=True)
        print(f"\n{self.player.name} board:")
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
                    return row, col

    def start_game(self):
        """
        Starts the battleship game.
        """
        try:
            self.welcome_message()
            self.get_player_name()

            self.place_ships(self.player_board)
            self.place_ships(self.computer_board)

            self.print_boards()

            is_player_turn = True

            while True:
                if is_player_turn:
                    print(f"\n{self.player.name}'s turn:")
                    row, col = self.get_guess(is_player_turn)

                    if row is None and col is None:
                        print("\nAborting the game... 3... 2... 1... Bye")
                        self.end_game()
                        break

                    if self.computer_board.board[row][col] == 'B':
                        print("You Hit!")
                        self.player.score += 1
                        self.computer_board.board[row][col] = '*'
                    else:
                        print("You Missed!")
                        self.computer_board.board[row][col] = 'X'
                else:
                    print("\nComputer's turn:")
                    row, col = self.get_guess(is_player_turn)

                    if self.player_board.board[row][col] == 'B':
                        print("The computer sank one of your battleships!")
                        self.player_board.board[row][col] = '*'
                        self.computer.score += 1
                    else:
                        print("The computer missed its guess.")
                        self.player_board.board[row][col] = 'X'

                print(f"{self.player.name}'s Score: {self.player.score}")
                print(f"COMPUTER's Score: {self.computer.score}")

                is_player_turn = not is_player_turn

                if self.player.score == 4:
                    print(f"\nCongratulations, {self.player.name}! You won!")
                    self.end_game()
                    break
                elif self.computer.score == 4:
                    print("The computer sank all your battleships! You lost!")
                    self.end_game()
                    break
                elif self.player.score > 2:
                    print("You are getting close!")

                self.print_boards()

        except Exception as e:
            print("An error occurred during the game:", str(e))
            self.end_game()

    def end_game(self):
        """
        Displays the end of the game and asks the player if
        they want to play again.
        """
        play_again = input("Do you want to play again? (yes/no):\n")
        if play_again.lower() == "yes":
            self.player.score = 0
            self.computer.score = 0
            self.player_board = Board()
            self.computer_board = Board()
            self.start_game()
        else:
            print("Thank you for playing Battleship Game!")


game = BattleshipGame()
game.start_game()
