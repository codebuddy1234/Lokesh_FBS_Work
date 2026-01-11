# Q3. Write a program to find sum of following series using functions:

# (c) 1¹ + 2² + 3³ + … + nⁿ

def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter n: "))
print("Sum =", sum_power(n))
