# Function to check if a number is an Armstrong number

def isArmstrong(a):
    '''
    Checks if a number is an Armstrong number.
    '''
    num_str = str(a)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == a

# Function calling
print(isArmstrong(153))
print(isArmstrong(123))

'''
Time complexity: O(d), where d is the number of digits in the integer.

Space complexity: O(1), as we are using a constant amount of space.
'''