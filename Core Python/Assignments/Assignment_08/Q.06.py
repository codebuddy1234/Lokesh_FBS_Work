# Q4. Sum of all odd numbers between 1 to n.

def sum_odd(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum  

n = int(input("Enter A Number: "))
print("Sum of Odd Numbers =",sum_odd(n))
