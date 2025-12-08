def fact(n):
    mult = 1
    for i in range(1, n + 1):
        mult *= i
    return mult

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(fact, data))
print(result)
