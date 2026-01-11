# Q2. Write a program to find maximum and minimum element in a list.

li =[1,-2,3,4,5]

max=li[0]
min=li[0]

for i in li:
    
    if i > max:
        max =i
    elif i < min:
        min =i 
    else:
        pass
print(f'MAX VALUE IN LIST :{max}')
print(f'MIN VALUE IN LIST :{min}')