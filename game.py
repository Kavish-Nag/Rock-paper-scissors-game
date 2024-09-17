import random
def game():
    ch=["rock","paper","scissors"]
    computer=random.choice(ch)
    
    user=input("Enter choice(rock, paper, scissors)")
    print("Computer choosed",computer)
    if user not in ch:
        print("Wrong input, please restart the game.")
        game()
    elif user==computer:
        print("It's a tie.")
        replay=input("Want to replay? (y/n)")
        if replay=="y" or replay=="Y":
            game()
        else:
            exit()
    elif (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper") or (user=="rock" and computer=="scissors"):
        print("You won!")
        replay=input("Want to replay? (y/n)")
        if replay=="y" or replay=="Y":
            game()
        else:
            exit()
    else:
        print("Computer wins!")
        replay=input("Want to replay? (y/n)")
        if replay=="y" or replay=="Y":
            game()
        else:
            exit()
game()
