from itertools import takewhile

def fib():
    """
    """
    a,b=0,1
    while 1:
        yield a
        a,b=b,a+b

print sum([i for i in takewhile(lambda x: x<4000000,fib()) if not i%2])    
