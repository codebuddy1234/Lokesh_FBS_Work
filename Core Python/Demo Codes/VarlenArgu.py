def add(*num):          # *num means we can pass multiple values
    sum = 0
    for val in num:
        sum = sum + val
    print("Sum =", sum)

# Example calls
add(10, 20)
add(1, 2, 3, 4, 5, 6, 7, 8, 9)
