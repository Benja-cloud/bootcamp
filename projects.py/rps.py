#import from the libraries
from random import randint

#create a list of play options
computer_options = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer_play = computer_options[randint(0,2)]

#set player instance to False
player = False

while player == False:
# flip and set player to True
    player = input("Rock, Paper, Scissors? Enter your choice:   ")
    print(f"You chose {player}, Computer chose {computer_play}.\n")

    if player == computer_play:
        print(" Its a Tie!!!")
    elif player == "Rock":
        if computer_play == "Paper":
            print("You lost!", computer_play, "covers", player)
        else:
            print("You are a winner!", player, "smashes", computer_play)
    elif player == "Paper":
        if computer_play == "Scissors":
            print("You lost!", computer_play, "cut", player)
        else:
            print("You are a winner!", player, "covers", computer_play)
    elif player == "Scissors":
        if computer_play == "Rock":
            print("You lost", computer_play, "smashes", player)
        else:
            print("You are a winner!", player, "cut", computer_play)
    else:
        print("That's not valid play. Kindly reconsider your spelling!")
    #player was set to True, so we make it be False for the loop to continue
    
    play_again = input("Want to play again? Y/N: ")
    if play_again.lower == "N":
        break 
    elif play_again == "Y":
        player = False
        computer_play = computer_options[randint(0,2)]