# Guess Battleship Game

## Overview
The Battleship Game is a classic board game where players try to sink each other's battleships by guessing the
coordinates on the opponent's board. In this game all you have to do is find computer's boats and sink them. 
Each boat has just one space in the board. After find 4 boats you win 

 ![New game](./Assets/Images/resposiviness.PNG) 


<br>

You can try here the [Live version](https://guess-battleship-game.herokuapp.com/)

<br>


# User Goals
 1. Enjoy a classic and engaging board game experience.
 2. Compete against the computer and try to outsmart it.
 3. Track their score and aim to achieve a high score.
 4. Have the flexibility to abort the game at any time.

## User Stories
1. As a user, I want to view the current state of the board and my opponent's board.
2. As a user, I want to make valid guesses and receive feedback on hits and misses.
3. As a user, I want to track my score and my opponent's score during gameplay.
4. As a user, I want to have the option to play again after the game ends.
## Scope
* The game should provide an interactive interface for players to enter their guesses.
* The game should validate user input and provide appropriate feedback.
* The game should track the scores of both the player and the computer.
* The game should have a clear termination condition and offer the option to play again.

# How to Play
The game begins with the placement of battleships on both the player's and the computer's board. Prior to that, the player encounters a welcome board with initial instructions on how to play the game. Just below the board, there is a designated space for the player to enter their name, which can be any combination of words, numbers, or a nickname.


![New game](./Assets/Images/new-game.PNG)



* Players take turns guessing the coordinates of the opponent's battleships. In the players board you will find a ("B").
It represents where players boats are positioned. 
If a guess hits an opponent's battleship, it is marked as a hit ('*'), and the player scores a point.
If a guess misses, it is marked as a miss ('X').


![Playing](./Assets/Images/playing.PNG)


* The game continues until one player manages to sink all of the opponent's battleships. Throughout the game, the player must determine the whereabouts of the computer's boats within the provided 30-space board. The board consists of 6 columns and 5 rows for the player to make guesses. Any guess outside the valid range of columns 1-6 and rows 1-5 will be considered an invalid guess and get a message informing that. 

![invalid](./Assets/Images/invalid-guess.PNG)

* The game will not allow the player to try the same guess. So if it happen a message will alert they that it was tried already to choose another guess. 

![Same Guess](./Assets/Images/same-guess.PNG)

* Players can abort the game by entering '9' as a guess.

![Aborting](./Assets/Images/aborting-game.PNG)

* The game also provides a real-time score board, displaying the score of each player after every guess.

![Score Board](./Assets/Images/score-board.PNG)

* The player who successfully guesses the positions of all four boats first wins the game. The game will display a congratulatory message and ask if the player wants to play again. Typing "yes" will initiate a new game and start the loop. Any other response will execute the end game function.

![end game](./Assets/Images/end-game.PNG)

<br>

# Features
## Existing Features
* Random placement of battleships on the board.
* Interactive gameplay where players alternate turns.
* Real-time feedback on hits, misses, and scores.
* Option to abort the game at any time.
* Play again feature after the game ends.

## Features to Implement
* Improved computer player logic for more strategic guesses.
* Graphical user interface (GUI) for a more engaging gaming experience.
* Difficulty levels to adjust the computer player's skill level.
* Multiplayer mode to play against another human player.

# Data Model

The game consists of the following classes:

* Board: Represents the game board and provides methods to print the board and place battleships.
* Player: Represents a player and stores their name, guesses, and score.
* BattleshipGame: The main game class that controls the gameplay and manages the player and computer boards.

# Testing
The Battleship Game has been tested extensively to ensure its functionality and accuracy. 
The code was passed through [PEP8 Python Validator](https://pep8ci.herokuapp.com/#) and no issues were found. The line lengths have been adjusted to adhere to the recommended maximum of 79 characters per line.

![end game](./Assets/Images/PEP8.PNG)

The following test cases were considered:

* Placing battleships randomly and ensuring they do not overlap.
* Validating user input for guesses and handling invalid inputs.
* Checking hits and misses during gameplay.
* Verifying game termination conditions.
* Abortion game option to execute end game or also start game again. 

## Solved Bugs
* Computers boats were displaying the board 
* Computers guesses were not getting ("*") sign when hit a right guess. 
* Game was not restarting as per request in the end of the game.


## Unsolved Bug
* If the player plays too fast, the turn of the computer player may be missed, leading to consecutive turns for the player.


# Deployment
Steps to deployment were followed from Code Institute learning material.

<br>

1. Sign in to your Heroku account.
2. Access the main page and click the "New" button in the top-right corner. Choose "Create New App" from the drop-down menu.
3. Choose a unique name for your app and select the region.
4. Once the app is created, go to the Deploy Tab and select the "Settings" Tab. Scroll down to "Config Vars".
5. Click "Reveal Config Vars" and enter "port" as the key, and "8000" as the value. Click "Add" to confirm the entry.
6. Next, enter your Google credentials into the "CREDS" key and value fields.
7. Go back to the Buildpack section and select "python", then click "Save Changes". Repeat this step to add "node.js", ensuring that the Buildpacks are in the correct order.
8. Go to the "Deploy" tab and select "Github" as the deployment method. Confirm that you want to connect to GitHub and search for the repository name.
9. Scroll to the bottom of the page and choose your preferred deployment type.
10. Finally, click "Manual Dedploy" or "Enable automatic update".

# Credits
This Battleship Game was created as an example by Felipe Zanetti for my 3rd milestone project. 
The game concept is based on the classic board game Battleship.
The [w3schools](https://www.w3schools.com/python/) were used for clarifications and updates. 
The deployment steps provided in this README were adapted from the Code Institute learning material.
Deployment


