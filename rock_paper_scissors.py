import random
while True:
    print("Let's play Rock Paper Scissors \n choose the option \n 1. Rock \n 2. Paper \n 3. Scissors")
    a=int(input("Enter your choice(eg-1,2,3)- "))
    b=random.randint(1,3)
    if int(a) == int(b):
        print("Draw",a,b)
    elif int(a)==1 and int(b)==2:
        print("you-Rock   Pc-Paper \n You lose, Paper beats Rock")
    elif int(a)==1 and int(b)==3:
        print("you-Rock   Pc-Scissors \n you won, rock beats scissors")
    elif int(a)==2 and int(b)==1:
        print("you-Paper   Pc-Rock \n you won, Paper beats Rock")
    elif int(a)==2 and int(b)==3:
        print("you-Paper   Pc-Scissors \n you lose, Scissors cuts Paper")
    elif int(a)==3 and int(b)==1:
        print("you-Scissors   Pc-Rock \n you lose, Rock beats Scissors")
    elif int(a)==3 and int(b)==2:
        print("you-Scissors   Pc-Paper \n you win, Scissors cuts paper")
    else:
        print("Invaid Selection")
    play_again=input("Do you want to play again,(y/n)- ")
    if play_again== "n":
        break