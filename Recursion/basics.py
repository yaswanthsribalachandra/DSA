#Recursion
# A function that calls itself is called a recursive function.
'''
infinite loop
def f():
    print("1")
    f()

f()
'''
count = 0
def f():
    '''This is a recursive function that prints numbers from 0 to 4.'''
    global count
    if(count==5):
        return
    print(count)
    count = count + 1
    f()
f()

#time complexity
# The time complexity of this function is O(n), where n is the value of count.
#space complexity
# The space complexity of this function is O(n), where n is the value of count.