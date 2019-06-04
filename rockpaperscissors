# System imports
# This was coded by ЧillehNation
# You may use this code and do whatever you like with it. Just don't call it yours.

import sys
import random, time
from os import system, name

#Default values for the game.
userScore = 0
compScore = 0
choices = ["r", "p", "s"]

#Sets var for pre game message to display once.
pre_game_msg = True

#Displays current score of both teams
def currentScore():
    print("Your score: " + str(userScore))
    print("Computer's score: " + str(compScore))

#Determines the score for both teams after each play
def finalDeterminer():
    if userScore == 3:
        print("\nUSER WINS THE GAME!")
        sys.exit()
    elif compScore == 3:
        print("\nBOT WINS THE GAME!")
        sys.exit()
    else:
        pass

#Asks user if they want to play again
def restartGame():
    user_pa = print("\n Play again? (y/n): ")
    if user_pa == "y" or "y".upper():
        userScore = 0
        botScore = 0
    elif user_pa == "n" or "n".upper():
        sys.exit()


        
###############################################################################
#Game start. Continue this code if both teams haven't won or done anything yet
###############################################################################



# Displays pre-game messgage
while pre_game_msg == True:
  if pre_game_msg == True:
      print('\nThis game only responds to \'r\', \'p\', \'s\' answers.'''
            '\nThis game is not designed to take unexpected answers.')
      pre_game_msg = False
  else:
        pass
#Start
while userScore != 3 or compScore != 3:

    # Bots chooses randomly from [choices]
    compChoice = random.choice(choices)
    disp_compChoice = print("\nYour computer chose: " + compChoice)

    # User chooses from [choices]
    userChoice = input("Your choice: ")


    #Determines if it's a tie & if not pass...
    if userChoice == compChoice:
        print("Tie. No Scores given.")
        userScore += 0
        compScore += 0
    else:
        pass

        # Determines if rock beats scissors
        if userChoice == "r" and compChoice == "s":
            print("You win this round Rock beats scissors")
            userScore = userScore + 1
            time.sleep(1)
            finalDeterminer()
            currentScore()


        elif userChoice== "s" and compChoice == "r":
            print("Bot wins. Rock beats scissors")
            compScore = compScore + 1
            time.sleep(1)
            finalDeterminer()
            currentScore()


        # Determines if paper beats rock.
        elif userChoice == "r" and compChoice == "p":
            print("Bot wins. Paper covers rock.")
            compScore = compScore + 1
            time.sleep(1)
            finalDeterminer()
            currentScore()


        elif userChoice == "p" and compChoice == "r":
            print("User wins. Paper covers rock.")
            userScore = userScore + 1
            time.sleep(1)
            finalDeterminer()
            currentScore()


        # Determines if scissors beats paper.
        elif userChoice == "s" and compChoice == "p":
            print("User wins. Scissors beats paper.")
            userScore = userScore + 1
            time.sleep(1)
            finalDeterminer()
            currentScore()


        elif userChoice == "p" and compChoice == "s":
            compScore = compScore + 1
            print("Bot wins. Scissors beats paper.")
            time.sleep(1)
            finalDeterminer()
            currentScore()

        #If all combinations fail display this
        else:
            print("There was a problem calculating with finalDeterminer.")
            sys.exit()
