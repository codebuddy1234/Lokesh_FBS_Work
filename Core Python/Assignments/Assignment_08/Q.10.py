# Q8. Write a program to find reverse of a number.

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input("Enter number: "))
print("Reverse =", reverse_number(n))

# n = int(input("Enter a number: "))

# temp = n
# sum = 0

# while (temp > 0):
#     dig = temp % 10
#     sum = (sum * 10) + dig
#     temp = temp // 10

# print(sum)
