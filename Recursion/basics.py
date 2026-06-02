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
    global count
    if(count==5):
        return
    print(count)
    count = count + 1
    f()
f()
