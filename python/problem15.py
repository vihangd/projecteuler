
# There are always 2n steps by using 2n!/(n! * n!)
# we can find out the no of paths
# http://www.joaoff.com/2008/01/20/a-square-grid-path-problem/

def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

def paths_for_grid_of(n):
    return (factorial(2*n))/(factorial(n)*factorial(n))

print paths_for_grid_of(20)
    
