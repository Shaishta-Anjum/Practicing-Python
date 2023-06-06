#Performance measuring Decorator
from time import time
def performance(fn):
    def wrap(*args,**kwrgs):
        t1=time()
        res=fn(*args,**kwrgs)
        t2=time()
        print(f'It took {t2-t1} s')
        return res
    return wrap

@performance
def long_time():
    for i in range(10000000):
        i*5
long_time()