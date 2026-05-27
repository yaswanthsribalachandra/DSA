# Function to get the elements and their indices

def indexing(arr):
    """Returns the elements and their indices in the given array."""
    if not arr:
        return []
    return [(i, arr[i]) for i in range(len(arr))]

# Function calling
print(indexing([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

'''
Time complexity: O(n), where n is the number of elements in the array.

Space complexity: O(n), as we are storing the elements and their indices in a list.
'''