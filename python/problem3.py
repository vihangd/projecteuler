
def is_prime(n):
    import math
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

no=600851475143
i=0
while i<int(600851475143/2)+1:
   i+=1
   if  not no%i :
       if is_prime(i):
           print i

