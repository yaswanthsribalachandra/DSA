# Function to compute the GCD of two numbers
def gcd(a, b):
    '''
    Computes the greatest common divisor (GCD) of two numbers.
    '''
    while b:
        a, b = b, a % b
    return a

# Function calling
print(gcd(48, 18))
print(gcd(101, 10))

'''
Time complexity: O(log(min(a, b))), where a and b are the two numbers.

Space complexity: O(1), as we are using a constant amount of space.
'''