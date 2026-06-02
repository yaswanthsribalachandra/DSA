# This is a recursive function that prints the name and a count from 0 to 4.

'''count = 0
def print_name(name):
    This is a recursive function that prints the name and a count from 0 to 4.
    global count
    if count == 5:
        return
    print(name, count)
    count = count + 1
    print_name(name)
print_name("John")
'''


def print_name(name, count):
    '''This is a recursive function that prints the name and a count from 0 to 4.'''
    if count == 5:
        return
    print(name, count)
    print_name(name, count + 1)
print_name("John", 0)

#time complexity
# The time complexity of this function is O(n), where n is the value of count.
#space complexity
# The space complexity of this function is O(n), where n is the value of count.
