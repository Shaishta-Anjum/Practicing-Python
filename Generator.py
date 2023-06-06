def gen():
    for i in range(10):
        yield i*5
        
for j in gen():
    print(j)
