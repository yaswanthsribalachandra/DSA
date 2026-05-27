# Function to check if an array is sorted
def isSorted(arr):
    '''
    Checks if the given array is sorted in non-decreasing order.
    '''
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Function calling
print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([5, 4, 3, 2, 1]))

'''
Time complexity: O(n), where n is the length of the array.

Space complexity: O(1), as we are using a constant amount of space.
'''