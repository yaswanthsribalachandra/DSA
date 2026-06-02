def print_nums(i,n):
    if i>n:
        return
    print(i)
    i= i + 1
    print_nums(i,n)
print_nums(1,5)