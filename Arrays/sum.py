# Find the sum of all numbers in an array

def array_sum(arr):
    """Returns the sum of all numbers in the given array."""
    sum=0
    for i in arr:
        sum = sum+i
    return sum

# Function calling
print("The sum of [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] is :", array_sum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
print("The sum of [] is :", array_sum([]))

'''
Time complexity: O(n), where n is the number of elements in the array.s

Space complexity: O(1), as we are using a constant amount of space.
'''