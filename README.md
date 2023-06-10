# Battleship Game
<br>

## Overview
The Battleship Game is a classic board game where players try to sink each other's battleships by guessing the
coordinates on the opponent's board. In this game all you have to do is find computers boats and sink them. 
Each boat has just one space in the board. After find 4 boats you win 
[]()
[Live version](https://guess-battleship-game.herokuapp.com/)
<br>

# How to Play
The game starts with the placement of battleships on both the player's and the computer's board.

[](new-game.PGN)
Players take turns guessing the coordinates of the opponent's battleships.
If a guess hits an opponent's battleship, it is marked as a hit ('*'), and the player scores a point.
If a guess misses, it is marked as a miss ('X').
[](playing.PNG)
The game continues until one player sinks all of the opponent's battleships.
Players can abort the game by entering '9' as a guess.
Features
Existing Features
Random placement of battleships on the board.
Interactive gameplay where players alternate turns.
Real-time feedback on hits, misses, and scores.
Option to abort the game at any time.
Play again feature after the game ends.
Features to Implement
Improved computer player logic for more strategic guesses.
Graphical user interface (GUI) for a more engaging gaming experience.
Difficulty levels for adjusting the computer player's skill level.
Multiplayer mode to play against another human player.
Data Model
The game consists of the following classes:

Board: Represents the game board and provides methods to print the board and place battleships.
Player: Represents a player and stores their name, guesses, and score.
BattleshipGame: The main game class that controls the gameplay and manages the player and computer boards.
Testing
The Battleship Game has been tested extensively to ensure its functionality and accuracy. The following test cases were considered:

Placing battleships randomly and ensuring they do not overlap.
Validating user input for guesses and handling invalid inputs.
Checking hits and misses during gameplay.
Verifying game termination conditions.
Testing the play again feature.
Solved Bugs
[Describe bugs that have been resolved during development.]
Unsolved Bug
If the player plays too fast, the turn of the computer player may be missed, leading to consecutive turns for the player.
Validator Testing
The code has been validated using PEP 8 guidelines, and no issues were found. The line lengths have been adjusted to adhere to the recommended maximum of 79 characters per line.

Credits
This Battleship Game was created as an example by [Your Name].
The game concept is based on the classic board game Battleship.
The deployment steps provided in this README were adapted from the Code Institute learning material.
Deployment
[Provide deployment instructions if applicable.]

User Goals
[Describe the user goals and requirements for the project.]

User Stories
As a user, I want to view the current state of the board and my opponent's board.
As a user, I want to make valid guesses and receive feedback on hits and misses.
As a user, I want to track my score and my opponent's score during gameplay.
As a user, I want to have the option to play again after the game ends.
Scope
The game should provide an interactive interface for players to enter their guesses.
The game should validate user input and provide appropriate feedback.
The game should display the current state of the board and update it after each guess.
The game should track the scores of both the player and the computer.
The game should have a clear termination condition and offer the option to play again.