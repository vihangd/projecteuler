import math

def list_primes(count):
    current=2
    test=0
    while current<=count:
        i = 1
        result=False
        while i <= math.sqrt(test):
            i += 1
            if not test % i:
                result=False
                break
            else:
                result=True
            
        if result:
            yield test
            current+=1
        test+=1
        


for i in list_primes(10001):
    print i 




            
        
