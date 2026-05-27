# Function to find all divisors of a number
def findDivisors(n):
    '''
    Finds all divisors of a given number.
    '''
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# Function calling
print(findDivisors(12))
print(findDivisors(25))

'''
Time complexity: O(sqrt(n)), where n is the number for which we are finding divisors.

Space complexity: O(d), where d is the number of divisors.
'''