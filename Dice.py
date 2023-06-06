t=int(input())
for i in range(t) :
       x, y = map(int, input().split())
       if (x+y)>=6:
            print("Yes")
       else:
            print("No")