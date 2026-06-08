#Function for flattening a nested list



'''def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


# Input
nested_list = [[1, 2], [3, [4, 5]], [6, [7, [8,[5, 9]]]]]

# Output
flattened = flatten_list(nested_list)
print(flattened)
'''

def flatten_list(lst):
    result = []

    for sublist in lst:
        for item in sublist:
            result.append(item)

    return result


lst = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(lst))




'''
time complexity: O(n)
space complexity: O(n)
'''