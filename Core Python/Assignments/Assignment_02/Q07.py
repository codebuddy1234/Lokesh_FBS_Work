# 7. Find the sum of three-digit number.

# take three digit number as input from user
num = int(input("Enter a three-digit number: "))
sum = 0

# perform operation to find sum of digits

d1 = num % 10 # get last digit
num = num // 10 # remove last digit

d2 = num % 10 # get second last digit
num = num // 10 # remove second last digit

d3 = num % 10 # get first digit
num = num // 10 # remove first digit

sum = d1 + d2 + d3
print(sum)