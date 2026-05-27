def countOddNumbers(arr):
    '''
    Counts the number of odd numbers in a given array.
    '''
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count

# Function calling
print(countOddNumbers([1, 2, 3, 4, 5]))
print(countOddNumbers([2, 4, 6, 8]))

'''
Time complexity: O(n), where n is the length of the array.

Space complexity: O(1), as we are using a constant amount of space.
'''