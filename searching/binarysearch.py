# Binary Search Algorithm

'''
the list should be sorted in ascending order before applying binary search.
'''


def binarysearch(arr,target):
    ''' this function implements binary search algorithm '''
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
a = binarysearch([1, 2, 3, 4, 5], 3)
print(a)

'''
timecomplexity
The time complexity of binary search is O(log n) because it divides the search interval in half with each iteration.

spacecomplexity
The space complexity of binary search is O(1) because it only requires a constant amount of additional memory space for the variables used in the algorithm.

'''