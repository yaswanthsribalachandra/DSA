def pattern6(n):
    '''Prints a right-angled triangle pattern of asterisks.'''
    for i in range(n):
        for j in range(n):
            if (i+j)<n:
                print("*", end="")
        print()

# Call the function
pattern6(5)

'''
output:
*****
****
***
**
*
'''

'''
time complexity: O(n^2)
space complexity: O(1)
'''