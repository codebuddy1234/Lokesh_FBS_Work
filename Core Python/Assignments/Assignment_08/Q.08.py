# Q6. Fibonacci series (n terms).

def fibonacci(n):
    a, b = 1, 1
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)
