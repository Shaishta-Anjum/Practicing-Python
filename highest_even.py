mylist=[1,2,4,6,82,26]
even=[]
for i in mylist:
    if i%2==0:
        even.append(i)
print(max(even))