# Pattern 1
def pattern1(n):
    ''' this function prints a pattern '''
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()
        
        
#Example
pattern1(5)

'''
time complexity
The time complexity of this pattern printing function is O(n^2) because there are two nested loops, each iterating n times.

space complexity
The space complexity of this pattern printing function is O(1) because it uses a constant amount of space for the loop variables.

'''