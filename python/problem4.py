
def is_palindrome(no):
    """
    
    Arguments:
    - `no`:
    """
    string_no=str(no)
    length=len(string_no)
    for i in range(0,length):
        if not string_no[i]==string_no[length-i-1]:
            return False
    return True

def calc_mul():
    for i in xrange(100,1000):
        for j in xrange(i,1000):
            mul=i*j
            if is_palindrome(mul):
                yield mul

if __name__ == '__main__':

    print max(calc_mul())
        
