
import math

def triag():
    i=0
    suma=0
    while 1:
        i+=1
        suma+=i
        yield suma


def get_factors(n):
    count = 0
    for x in xrange(1, int(math.sqrt(n)+1)):
        if not n%x:
            count += 2
    return count
    


for i in triag():
    if get_factors(i) > 500:
        print i
        break



    


    
    

