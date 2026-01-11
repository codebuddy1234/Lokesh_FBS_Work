# Q2. Write a program to calculate area of circle.

def area_circle(R):
    a = lambda r : 3.14 * r * r
    return a(R)

x = int(input("Enter A Radius: "))
print("Area of Circle",area_circle(x))
