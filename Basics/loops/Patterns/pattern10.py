def pattern10(n):
    '''Prints a right-angled triangle pattern of asterisks.'''
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
        print()

    '''Prints a right-angled triangle pattern of asterisks.'''
    for i in range(n):
        for j in range(n):
            if (i+j)<n:
                print("*", end="")
        print()
# Call the function
pattern10(5)



'''
output:
*
**
***
****
*****
*****
****
***
**
*
'''

'''
time complexity: 2*O(n^2)
space complexity: 2*O(1)
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

