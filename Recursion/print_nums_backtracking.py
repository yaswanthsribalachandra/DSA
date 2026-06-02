def print_nums(i,n):
    if i<1:
        return
    print_nums(i-1,n)
    print(i)
print_nums(5,5)