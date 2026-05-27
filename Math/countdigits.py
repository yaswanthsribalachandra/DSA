# Function to count the number of digits in an integer
def countDigits(n):
    '''
    Counts the number of digits in a given integer.
    '''
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

# Function calling
print(countDigits(12345))
print(countDigits(100))

'''
Time complexity: O(d), where d is the number of digits in the integer.

Space complexity: O(1), as we are using a constant amount of space.
'''