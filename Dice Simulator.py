# -*- coding: utf-8 -*-
#Created on Thu Jun 11 18:41:32 2020
#@author: Siyolise Solani

"""This is a Rolling dice simulator.

Importing a random module allows the dice to ouput random number 
between 1 and 6 when the function randint() is used,

and importing sys module enables the program to exit when user wants to."""

import random
import sys

print("Welcome to Rolling Dice Simulator Game") #prints the welcoming part
#The progam allows two players, human and a computer.
human = ""
computer = ""
game_is_on = True

#This while-loop allows repetitive actions to occur whilst  the game is on.
#Human gets to decide whether they want to play first or not.
#If human inputs NO, then the computer plays.

while True:
    human_input = input("Do you wanna roll first? Enter 'YES' or 'NO': ").upper()
    roll_dice = random.randint(1,6)
    
    if human_input == "YES":
        print("Human is playing and the dice is rolling....")
        print(f"OK the dice has been rolled and your output is {roll_dice}.")
        continue
        
    else:
        print("Computer is playing and the dice is rolling....")
        print(f"Computer's output is {roll_dice}.")
        
    human_replay = input("Enter 'R' to restart or 'X' to exit the game: ").upper()
    
    if human_replay == "R":
        print("Let's play Again")    #human restarts the program
        continue
    
    elif human_replay == 'X':
        print("Goodbye!")
        sys.exit()         #The program exits.
        


