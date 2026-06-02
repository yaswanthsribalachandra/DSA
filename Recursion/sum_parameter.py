# This is a recursive function that calculates the sum of first n natural numbers.
def sum_nums(i,sum):
    if i<1:
        print(sum)
        return
    sum = sum + i
    sum_nums(i-1,sum)
n = 5
print("Sum of first",n,"natural numbers is: ",end="")
sum_nums(n,0)

#time complexity
# The time complexity of this function is O(n), where n is the value of n.
#space complexity
# The space complexity of this function is O(n), where n is the value of n.