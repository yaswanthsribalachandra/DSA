def pattern8(a):
    n=a
    '''Prints a downward triangle pattern of asterisks.'''
    for i in range(n):
        for k in range(i):
            print(end=" ")
        mul = (2*(n-i))-1
        print(mul*"*", end="")
        print()
# Call the function
pattern8(5)

'''
output:

*********
 *******
  *****
   ***
    *

time complexity: O(n^2)
space complexity: O(1)
'''