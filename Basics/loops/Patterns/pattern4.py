def pattern4(n):
    '''Prints a right-angled triangle pattern of numbers.'''
    for i in range(n):
        for j in range(n):
            if j <= i:
                print(i + 1, end=" ")
        print()

# Call the function
pattern4(5)

'''
output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

'''
time complexity: O(n^2)
space complexity: O(1)
'''

