file=open('problem13.txt')
sum=0
for line in file:
    sum+=int(line.strip())
print str(sum)[:10]
