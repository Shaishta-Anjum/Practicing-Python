#Write a program which can compute the factorial of a given numbers.
def fact(n):
    if (n==0) or (n==1):
        return 1
    else:
        return (n*fact(n-1))
x=int(input("Enter number:"))
print("Factorial of",x,"is",fact(x))