def print_rev_nums(i,n):
    if i>n:
        return
    print(n,end=" ")
    print_rev_nums(i,n-1)
print_rev_nums(1,5)
print()