# write a program that lets the user of the game play rock paper scissors against
# the computer
# 10/1/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Jerome Pinckney
#

#get rock paper or scissors from user
user = input('Enter rock, paper or scissors: ')
rock = 1
paper = 2
scissor = 3

# computer choses a number between 1 and 3
import random
computer = random.randrange(1, 4)

# get user to enter rock, paper or  scissors
def main():
    user_()
    
# goes through different combinations based on what the computer chose
def user_():
    if computer == 1:
        if user == 'rock':
            print('computer chose rock')
            print('tie')
        elif user == 'paper':
            print('computer chose rock')
            print('you win')
        else:
            print('computer chose rock')
            print('you lose')
    elif computer == 2:
        if user == 'rock':
            print('computer chose paper')
            print('you lose')
        elif user == 'paper':
            print('computer chose paper')
            print('tie')
        else:
            print('computer chose paper')
            print('you win')
    else:
        if user == 'rock':
            print('computer chose scissors')
            print('you win')
        elif user == 'paper':
            print('computer chose scissors')
            print('yoou lose')
        else:
            print('computer chose scissor')
            print('tie')

#call main function
main()
