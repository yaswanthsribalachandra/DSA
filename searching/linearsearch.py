# Linear Search Algorithm

def linear_search(arr, target):
    ''' this function implements linear search algorithm '''
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Example usag
a = linear_search([1, 2, 3, 4, 5], 3)
print(a)

'''
timecomplexity
The time complexity of linear search is O(n) because it may need to check each element in the list in the worst case.

spacecomplexity
The space complexity of linear search is O(1) because it only requires a constant amount of additional memory space for the variables used in the algorithm.

'''