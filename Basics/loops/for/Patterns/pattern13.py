def pattern13(n):
    '''Prints a right-angled triangle pattern of numbers.'''
    k=1
    for i in range(n):
        for j in range(n):
            if j <= i:
                print(k, end=" ")
                k=k+1
        print()

# Call the function
pattern13(5)

'''
output:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15


time complexity: O(n^2)
space complexity: O(1)
'''
