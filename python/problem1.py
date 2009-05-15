
def return_val():
    """
    """
    for i in range(1,1000):
        if not  i%3 or not i%5:
            yield i

if __name__ == '__main__':
    print sum(return_val())
