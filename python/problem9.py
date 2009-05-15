

for a in xrange(1,1001):
    for b in xrange(a,1001):
        for c in xrange(b,1001):
            if a + b + c == 1000:
                c_sq=c*c
                if (a*a)+(b*b)==c_sq:
                    print a * b *c
