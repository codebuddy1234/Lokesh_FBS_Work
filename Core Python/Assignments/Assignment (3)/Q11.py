# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

Ticket = int(input("Enter the Ticket Amount: "))
age1=int(input("Enter age1 : "))
age2=int(input("Enter age2 : "))
age3=int(input("Enter age3 : "))
age4=int(input("Enter age4 : "))
age5=int(input("Enter age5 : "))


#age1
if (age1<12):
    price1 =Ticket - Ticket*0.30
elif(age1>59):
    price1 =Ticket - Ticket*0.50
else:
    price1=Ticket  

#age2      
if (age2<12):
    price2 =Ticket - Ticket*0.30
elif(age2>59):
    price2 =Ticket - Ticket*0.50
else:
    price2=Ticket  

#age3      
if (age3<12):
    price3 =Ticket - Ticket*0.30
elif(age3>59):
    price3 =Ticket - Ticket*0.50
else:
    price3=Ticket   

#age4     
if (age4<12):
    price4 =Ticket - Ticket*0.30
elif(age4>59):
    price4 =Ticket - Ticket*0.50
else:
    price4=Ticket   

#age5     
if (age5<12):
    price5 =Ticket - Ticket*0.30
elif(age5>59):
    price5 =Ticket - Ticket*0.50
else:
    price5=Ticket    

        
Total_Amount = price1+price2+price3+price4+price5
print(f'The total fare of 5 peoples is : {Total_Amount}')


