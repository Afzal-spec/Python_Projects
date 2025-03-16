import random


while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()
    
    if computer == player:
        print("computer: " + computer)
        print("Player: "+player)
        print("its a tie!")
    
    elif player == "scissors":
        if computer == "rock":
            print("computer: " + computer)
            print("Player: "+player)
            print("you lose!")
        else :
            print("computer: " + computer)
            print("Player: "+player)
            print("you win!")

    elif player == "rock":
        if computer == "paper":
            print("computer: " + computer)
            print("Player: "+player)
            print("you lose!")
        else :
            print("computer: " + computer)
            print("Player: "+player)
            print("you win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: " + computer)
            print("Player: "+player)
            print("you lose!")
        else :
            print("computer: " + computer)
            print("Player: "+player)
            print("you win!")


    play_again = input("do you want to play again? (yes/no): ").lower()
    if(play_again != "yes"):
        break
print("bye!")


    


