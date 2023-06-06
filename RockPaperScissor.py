import random
print("Welcome to the game of ROCK PAPER SCISSOR!!")
print("\nThere will be 5 rounds of this game and the Rules for winning this game are:\n1.Rock wins against Scissors\n2.Paper wins against Rock ")
print("3.Scissor wins against Paper\n4.It's a tie if both the inputs are same\n5.Enter 4 to Exit")
for i in range(5):
    comp=random.randint(1,3)
    n=int(input("\nEnter your choice:"))
    score=0
    comp_score=0
    if n==comp:
        print("Tie!!")
    elif n==4:
        break
    elif n==1:
        if comp==2:
            print("You Lose!! Paper covers Rock")
            comp_score+=1
        else:
            print("You Win!! Rock smash Scissor")
            score+=1
    elif n==2:
        if comp==1:
            print("You Win!! Paper covers Rock")
            score+=1
        else:
            print("You Lose!! Scissor cuts Paper")
            comp_score+=1
    elif n==3:
        if comp==1:
            print("You Lose!! Rock smash Scissor")
            comp_score+=1
        else:
            print("You Win!!Scissor cuts Paper")
            score+=1
    else:
        print("ERROR: Enter valid option")

if score>comp_score:
    print("\nYou WIN this game with a total of",score,"scores")
elif comp_score>score:
    print("\nYou lose:( with",score,"scores. Better Luck Next Time!!")
else:
    print("\nIt's a Tie")