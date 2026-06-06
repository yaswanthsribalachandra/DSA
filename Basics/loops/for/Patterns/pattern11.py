def pattern11(n):
    '''Prints a right-angled triangle pattern of numbers.'''
    for i in range(n):
        for j in range(n):
            if j <= i:
                print((i+j+1)%2, end=" ")
        print()

# Call the function
pattern11(5)

'''
output:


1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 

time complexity: O(n^2)
space complexity: O(1)
'''
