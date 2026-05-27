# Function to reverse a number

def reverse(a):
    '''
    Reverses the digits of an integer.
    '''
    reversed_num = 0
    while a > 0:
        digit = a % 10
        reversed_num = reversed_num * 10 + digit
        a //= 10
    return reversed_num

# Function calling
print(reverse(12345))
print(reverse(100))

'''
Time complexity: O(d), where d is the number of digits in the integer.

Space complexity: O(1), as we are using a constant amount of space.
'''