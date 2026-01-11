# Q3. Write a program to find the second largest element in the list.

li=[1,2,3,4,5,10]

larg1 = li[0]
larg2 = li[0]

for i in li:
    if i > larg1:
        larg2 = larg1
        larg1 = i
    elif i < larg1 and larg2 != larg1:
        larg2 = i 
        
print(larg1)
print(larg2)