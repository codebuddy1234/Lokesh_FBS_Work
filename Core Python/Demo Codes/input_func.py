A = input("Enter Anything to print: ")
#directly printing the input value 
#using variable A because input function not type directly in print function

print("Entered Value is :",A)
print("type of A value is:",type(A))

# input function always takes input in string format
# so if we want to take integer input we have to convert it into integer using int()

B = int(input("Enter Integer Value to print: "))
print("Entered Integer Value is :",B)
print(type(B))