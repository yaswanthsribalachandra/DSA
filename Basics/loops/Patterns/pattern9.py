def pattern7(a):
    n=a
    '''Prints a upward triangle pattern of asterisks.'''
    for i in range(n):
        for k in range(n-i-1):
            print(end=" ")
        mul = (2*i)+1
        print(mul*"*", end="")
        print()
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
pattern7(5)
pattern8(5)

'''
output:
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
    


 time complexity: 2*O(n^2)
space complexity: 2*O(1)
'''