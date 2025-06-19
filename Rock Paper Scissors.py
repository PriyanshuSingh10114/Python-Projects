"""TASK 4 - ROCK-PAPER-SCISSORS GAME"""

import random
while True:
    print("Enter 1 for ROCK")
    print("Enter 2 for PAPER")
    print("Enter 3 for SCISSORS")
    user_choice=int(input("user choice :"))
    if(user_choice>3 or user_choice<=0):
        print("INVALID INPUT ...YOU/USER LOSE")
    else:
        computer_choice=random.randint(1,3)
        print("computer's choice :",computer_choice)

    """RULES OF THE GAME"""
    #ROCK(1) AND PAPER(2)-->PAPER(2) WINS 
    #PAPER(2) AND SCISSORS(3)-->SCISSORS(3) WINS
    #ROCK(1) AND SCISSORS(3)-->ROCK(1) WINS

    if(user_choice==computer_choice):
        print("Its a TIE")
    elif(user_choice==1 and computer_choice==2): #computer wins
        print("USER LOSE!!!")
    elif(user_choice==1 and computer_choice==3): #user wins
        print("USER WINS!!!")
    elif(user_choice==2 and computer_choice==1): #user wins
        print("USER WINS!!!")
    elif(user_choice==2 and computer_choice==3): #computer wins
        print("USER LOSE!!!")
    elif(user_choice==3 and computer_choice==1): #computer wins
        print("USER LOSE!!!")
    elif(user_choice==3 and computer_choice==2): #user wins
        print("USER WINS!!!")

    play_again=input("Want to play again?(Y/N) :")
    if play_again!="Y":
        print("Thanks for playing!!!")
        break
