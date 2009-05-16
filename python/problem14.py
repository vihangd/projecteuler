
series={}

def series_count(n):
    count=1
    n_org=n
    while n >1:
        if not n %2:
            n=n/2
        else:
            n=(3*n)+1
        count+=1
        if n in series:
            return count+series[n]
    series[n_org]=count
    return count


maxc=0

for i in xrange(1000000,1,-1):
     curr=series_count(i)
     if curr>maxc:
         maxc=curr
         max_i=i

print maxc,max_i




    


            
        

    
