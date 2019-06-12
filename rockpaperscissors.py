# System imports
# This was coded by ЧillehNation
# You may use this code and do whatever you like with it. Just don't call it yours.

import sys
import random
import time
from os import system, name

# Default values for the game.
userScore = 0
compScore = 0
choices = ["r", "p", "s"]

# Sets var for pre game message to display once.
pre_game_msg = True


# Displays current score of both teams
def currentScore():
    print("Your score: " + str(userScore))
    print("Computer's score: " + str(compScore))


# Determines the score for both teams after each play
def finalDeterminer():
    if userScore == 3:
        print("\nUSER WINS THE GAME!")
        restartGame()
    elif compScore == 3:
        print("\nBOT WINS THE GAME!")
        restartGame()

# Asks user if they want to play again
def restartGame():
    user_pa = input("\n Play again? (y/n): ")
    if user_pa == "y" or "y".upper():
        global userScore, compScore
        userScore = 0
        compScore = 0
    if user_pa == "n" or "n".upper():
        sys.exit()

def doAllShit():
    time.sleep(1)
    finalDeterminer()
    currentScore()


###############################################################################
# Game start. Continue this code if both teams haven't won or done anything yet
###############################################################################


# Displays pre-game message

print('\nThis game only responds to \'r\', \'p\', \'s\' answers.\nThis game is not designed to take unexpected answers.')

# Start
while userScore != 3 or compScore != 3:
    # Bots chooses randomly from [choices]
    compChoice = random.choice(choices)
    print("\nYour computer chose: " + compChoice)

    # User chooses from [choices]
    userChoice = input("Your choice: ")

    # Determines if it's a tie & if not pass...
    if userChoice == compChoice:
        print("Tie. No Scores given.")
        userScore += 0
        compScore += 0
        # Determines if rock beats scissors

    if userChoice == "r" and compChoice == "s":
        print("You win this round Rock beats scissors")
        userScore += 1
        doAllShit()
    if compChoice == "r" and userChoice == "s":
        print("Bot wins. Rock beats scissors")
        compScore += 1
        doAllShit()

    # Determines if paper beats rock.
    if userChoice == "r" and compChoice == "p":
        print("Bot wins. Paper covers rock.")
        compScore = compScore + 1
        doAllShit()
    if userChoice == "p" and compChoice == "r":
        print("User wins. Paper covers rock.")
        userScore += 1
        doAllShit()

    # Determines if scissors beats paper.
    if userChoice == "s" and compChoice == "p":
        print("User wins. Scissors beats paper.")
        userScore += 1
        doAllShit()
    if userChoice == "p" and compChoice == "s":
        compScore += 1
        print("Bot wins. Scissors beats paper.")
        doAllShit()
