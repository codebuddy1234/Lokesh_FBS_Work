# Q1. Write a program to calculate area of rectangle.

def area_rec(l,b):
    a= lambda l, b : l * b
    return a(l, b)

x = int(input("Enter A Length: "))
y = int(input("Enter A Breadth: "))
print(area_rec(x, y),'sq.cm')
