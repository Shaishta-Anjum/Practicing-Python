mylist=['a','b','c','f','g','b','i','l','g']
dupes=[]
for items in mylist :
    if mylist.count(items)>1:
        if items not in dupes:
            dupes.append(items)
print(dupes)

x="Hello"
lst=[char for char in x]
dupes=list(set([d for d in ['a','n','c','a','b','l','l'] if ['a','n','c','a','b','l','l'].count(d)>1]))
print(dupes)