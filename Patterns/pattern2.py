#Pattern 2

def pattern2(n):
    '''Prints a right-angled triangle pattern of asterisks.'''
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
        print()

# Call the function
pattern2(5)

'''
time complexity: O(n^2)
space complexity: O(1)
'''