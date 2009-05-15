
def fib():
    a,b=0,1
    while 1:
        yield a
        a,b=b,b+a

count=0
for i in fib():
    if len(str(i)) == 1000:
        print count
        break
    count+=1
