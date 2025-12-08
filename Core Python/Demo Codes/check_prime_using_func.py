def checkprime(num):
    for i in range(2,num//2+1):
        if(num%i==0):
            return False
        return True
n=int(input("Enter number to check whether its prime or not : "))
print(checkprime(n))