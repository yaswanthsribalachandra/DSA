# This is a recursive function that calculates the sum of first n natural numbers.
def sum_fun(n):
    '''This is a recursive function that calculates the sum of first n natural numbers.'''
    if n<=1:
        return n 
    return n + sum_fun(n-1)
print("Sum of first 5 natural numbers is: ",sum_fun(5))

#time complexity
# The time complexity of this function is O(n), where n is the value of n.
#space complexity
# The space complexity of this function is O(n), where n is the value of n.

