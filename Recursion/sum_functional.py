def sum_fun(n):
    if n<=1:
        return n 
    return n + sum_fun(n-1)
print("Sum of first 5 natural numbers is: ",sum_fun(3))