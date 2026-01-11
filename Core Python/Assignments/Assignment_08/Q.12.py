# Q11. WAP to check if a given number is Armstrong or not.

def is_armstrong(num):
    digits = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num

n = int(input("Enter number: "))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# n = int(input("Enter a number: "))

# temp = n
# sum = 0

# while (temp > 0):
#     dig = temp % 10
#     sum = sum + (dig ** 3)
#     temp = temp // 10

# if(sum == n):
#     print("the given number is ArmStrong")
# else:
#     print("the given number is not ArmStrong")
