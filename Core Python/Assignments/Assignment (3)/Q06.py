# 6. Write a program to calculate profit or loss.
sp=int(input("Enter selling price: "))
cp=int(input("Enter cost price: "))

profit=sp-cp
loss = cp-sp

if(sp>cp):
    print(f'our profit is : {profit} Rs')
elif(cp>sp):
    print(f'our loss is : {loss} Rs')   
else:
    print(f'NO profit NO loss')     