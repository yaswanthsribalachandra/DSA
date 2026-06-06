def pattern3(n):
    '''Prints a right-angled triangle pattern of numbers.'''
    for i in range(n):
        for j in range(n):
            if j <= i:
                print(j + 1, end=" ")
        print()

# Call the function
pattern3(5)

'''
output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

'''
time complexity: O(n^2)
space complexity: O(1)
'''

