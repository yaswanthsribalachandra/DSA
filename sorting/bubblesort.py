# Bubble Sort Algorithm

def bubblesort(arr):
    ''' this function implements bubble sort algorithm '''
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = bubblesort([64, 34, 25, 12, 22, 11, 90])
print(a)

''' 
timecomplexity
The time complexity of bubble sort is O(n^2) in the worst and average case,
and O(n) in the best case (when the array is already sorted).

Space complexity
The space complexity of bubble sort is O(1) because it only requires a constant amount of additional memory space for the variables used in the algorithm.

'''