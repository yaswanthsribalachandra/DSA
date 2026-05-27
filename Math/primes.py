# Function to check if a number is prime
def isPrime(a):
    '''Checks if a number is prime.'''
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

# Function calling
print(isPrime(11))
print(isPrime(4))

'''
Time complexity: O(sqrt(n)), where n is the number being checked.

Space complexity: O(1), as we are using a constant amount of space.
'''