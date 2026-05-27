# Function to check if a number is a palindrome

def isPalindrome(a):
    '''
    Checks if a number is a palindrome.
    '''
    original = a
    reversed_num = 0
    while a > 0:
        digit = a % 10
        reversed_num = reversed_num * 10 + digit
        a //= 10
    return original == reversed_num

# Function calling
print(isPalindrome(121))
print(isPalindrome(123))

'''
Time complexity: O(d), where d is the number of digits in the integer.

Space complexity: O(1), as we are using a constant amount of space.
'''