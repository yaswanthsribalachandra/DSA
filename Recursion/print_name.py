
'''count = 0
def print_name(name):
    global count
    if count == 5:
        return
    print(name, count)
    count = count + 1
    print_name(name)
print_name("John")
'''


def print_name(name, count):
    if count == 5:
        return
    print(name, count)
    print_name(name, count + 1)
print_name("John", 0)