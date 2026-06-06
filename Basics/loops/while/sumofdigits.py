# Program to find the sum of digits of a number
num = int(input("Enter a number: "))

def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

result = sum_of_digits(num)
print("Sum of digits:", result)

'''
expected output:
Enter a number: 123
Sum of digits: 6

time complexity: O(d), where d is the number of digits in the input number.
space complexity: O(1)
'''
