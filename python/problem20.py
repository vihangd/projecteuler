
def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

digits=str(factorial(100))
print digits
i=0
sum=0
for i in digits:
    sum+=int(i)

print sum
    
    
    
