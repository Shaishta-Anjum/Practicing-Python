print(list(map(lambda list:list*2,[2,4,6])))
print(list(map(lambda list:list**2,[1,2,3,4])))

a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x:x[1])
print(a)