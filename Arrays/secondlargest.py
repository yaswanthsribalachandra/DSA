# Function to find the second largest element in an array

def secondlargest(arr):
    """Returns the second largest number in the given array."""
    if not arr or len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

# Function calling
print(secondlargest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

'''
Time complexity: O(n), where n is the number of elements in the array.

Space complexity: O(1), as we are using a constant amount of space.
'''

