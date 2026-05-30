# Find the minimum number in an array

def minimum(arr):
    """Returns the minimum number in the given array."""
    if not arr:
        return None
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

# Function calling
print(minimum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

'''
Time complexity: O(n), where n is the number of elements in the array.

Space complexity: O(1), as we are using a constant amount of space.
'''