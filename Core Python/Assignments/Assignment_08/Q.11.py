# Q9. Write a program to check if entered number is a palindrome.

def is_palindrome(num):
    return num == reverse_number(num)

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input("Enter number: "))
if is_palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# n = int(input("Enter a number: "))

# temp = n
# rev = 0

# while (temp > 0):
#     dig = temp % 10
#     rev = rev * 10 + dig
#     temp = temp // 10

# if rev == n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
