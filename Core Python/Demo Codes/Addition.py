#Addition of two numbers

# input is always in string format then convert into int()
num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))

print("type of num1 is:",type(num1))
print("type of num2 is:",type(num2))

#adding two numbers
sum = num1 + num2

print("Addition of num1 and num2 is :", sum) # directly print addition value

print('Addition of ',num1,'and', num2, 'is :',sum ) # simply print add value with variable using ,separator

print('Addition of {} and {} is : {}'.format(num1,num2,sum)) # print addition value using format function

print(f'Addition of {num1} and {num2} is : {sum}') # print addition value using f string 

print("Addition of " + str(num1) + " and " + str(num2) + " is : " + str(sum)) # print addition value using concatenation

print("type of sum is:",type(sum)) # print type of sum value




# Now let's see what happens if we do not convert input into int()


input1 = input("Enter first number:")
input2 = input("Enter Second number:")

sum2 = input1 + input2
print("Addition of input1 and input2 is :", sum2)
print("type of sum2 is:",type(sum2))

# Here we can see that the addition of two numbers is not correct because input function takes input in string format
# so we have to convert it into integer using int() function


