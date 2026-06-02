def sum_nums(i,sum):
    if i<1:
        print(sum)
        return
    sum = sum + i
    sum_nums(i-1,sum)
n = 5
print("Sum of first",n,"natural numbers is: ",end="")
sum_nums(n,0)