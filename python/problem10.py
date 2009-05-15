def is_prime(n):
    import math
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
     i=2
     sum=0
     while 1:
         if is_prime(i):
             sum+=i
         if i==2000000:
             break
         i+=1

     print sum
