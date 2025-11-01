# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

Male_age = int(input("Enter the age of male: "))
Women_age = int(input("Enter the age of Women: "))

if(Male_age>=21 and Women_age>=18):
    print("Both are eligible for marriage")
else:
    print("both are underage")    
