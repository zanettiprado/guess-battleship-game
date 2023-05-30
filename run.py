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


# Nessa função eu arrumo a matriz para parecer um tabuleiro de batalha naval

#places the player boats

#place computer boats

#shots from the player 

#shots from the computer 

#ships remaining

#end game 


