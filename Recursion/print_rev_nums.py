# This is a recursive function that prints numbers from n to 1.
def print_rev_nums(i,n):
    '''This is a recursive function that prints numbers from n to 1.'''
    if i>n:
        return
    print(n,end=" ")
    print_rev_nums(i,n-1)
print_rev_nums(1,5)
print()

#time complexity
# The time complexity of this function is O(n), where n is the value of n.
#space complexity
# The space complexity of this function is O(n), where n is the value of n.
