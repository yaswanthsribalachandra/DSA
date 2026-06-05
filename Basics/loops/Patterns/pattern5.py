def pattern5(n):
    '''Prints a right-angled triangle pattern of numbers.'''
    for i in range(n):
        for j in range(n):
            if (i+j)<n:
                print(j + 1, end=" ")
        print()

# Call the function
pattern5(5)

'''
output:
12345
1234
123
12
1
'''

'''
time complexity: O(n^2)
space complexity: O(1)
'''