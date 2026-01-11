# Q10. Check if entered year is leap year or not.

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter year: "))
if is_leap_year(year):
    print("Leap Year")
else:
    print("Not a Leap Year")


# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")
