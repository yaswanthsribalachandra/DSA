# This is a recursive function that prints numbers from n to 1. backtracking
def print_nums(i,n):
    '''This is a recursive function that prints numbers from n to 1.'''
    if i<1:
        return
    print_nums(i-1,n)
    print(i)
print_nums(5,5)

#time complexity
# The time complexity of this function is O(n), where n is the value of n.
#space complexity
# The space complexity of this function is O(n), where n is the value of n.