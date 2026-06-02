#Print reverse numbers from n to 1
def print_rev_nums(i,n):
    if i>n:
        return
    print_rev_nums(i+1,n)
    print(i)
print_rev_nums(1,5)
print()