
dict ={1: "one",
       2: "two",
       3: "three",
       4: "four",
       5: "five",
       6: "six",
       7: "seven",
       8: "eight",
       9: "nine",
       10: "ten",
       11: "eleven",
       12: "twelve",
       13: "thirteen",
       14: "fourteen",
       15: "fifteen",
       16: "sixteen",
       17: "seventeen",
       18: "eighteen",
       19: "nineteen",
       20: "twenty",
       30: "thirty",
       40: "forty",
       50: "fifty",
       60: "sixty",
       70: "seventy",
       80: "eighty",
       90: "ninety",
       100: "hundred",
       1000: "onethousand"}

def two_digits(n):
    for j in range(20,100+10,10):
        if n < j:
            string=str(n)
            return dict[j-10]+dict[int(string[1])]



final_string=""

for i in xrange(1,1000+1):
    if i in dict:
        if i==100:
            final_string+= "one"
        final_string+= dict[i]
    else:
        if len(str(i))<3:
            final_string+= two_digits(i)
        else:
            string=str(i)
            last_two=int(string[1:])
            first=int(string[0])
            if last_two in dict:
                final_string+= dict[first]+dict[100]+"and"+dict[last_two]
            elif last_two==0:
                final_string+=  dict[first]+dict[100]
            else:
                final_string+= dict[first]+dict[100]+"and"+two_digits(int(last_two))

print len(final_string)
