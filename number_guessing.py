import random
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
x=random.randint(lower,upper)
print("Guess the Random Number in 10 tries. Good Luck!!")
for i in range(10):
    guess=int(input("Enter your guess:"))
    if guess<x:
        print("You guessed too small.")
    elif guess>x:
        print("You guessed too high")
    elif guess==x:
        print("Congratulations!! You guessed it right this time.")
        break
    else:
        print("Better Luck next time !!")