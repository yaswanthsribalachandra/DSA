# Find the largest number in an array

def largest(arr):
    """Returns the largest number in the given array."""
    if not arr:
        return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# Function calling
print(largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

'''
Time complexity: O(n), where n is the number of elements in the array.

Space complexity: O(1), as we are using a constant amount of space.
'''