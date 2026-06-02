# This is a recursive function that prints numbers from 1 to n.
def print_nums(i,n):
    '''This is a recursive function that prints numbers from 1 to n.'''
    if i>n:
        return
    print(i)
    i= i + 1
    print_nums(i,n)
print_nums(1,5)

#time complexity
# The time complexity of this function is O(n), where n is the value of n.
#space complexity
# The space complexity of this function is O(n), where n is the value of n.