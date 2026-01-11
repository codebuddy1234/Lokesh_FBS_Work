# Q7. Write a program to find sum of digits of a number using function.

def sum_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

n = int(input("Enter number: "))
print("Sum of digits =", sum_digits(n))
