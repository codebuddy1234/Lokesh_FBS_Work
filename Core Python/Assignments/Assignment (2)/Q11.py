# 11. Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount. 

Amount = int(input("Enter The amount : "))
TwoThousand = Amount//2000
Remain1= Amount - 2000*TwoThousand
Temp = Amount%2000
Fivehundred = Temp//500
Remain2= Remain1 - 500*Fivehundred
Temp = Temp%500
Twohundred = Temp // 200
Remain3 = Remain2 - 200*Twohundred
Temp = Temp % 200
hundred = Temp//100
Remain4= Remain3 - 100*hundred
Temp = Temp % 100
fifty = Temp //50
Remain5= Remain4 - 50*fifty
Temp = Temp % 50
Twenty = Temp//20
Remain6 = Remain5 -20*Twenty
Temp = Temp % 20
Ten = Temp//10
Remain7 = Remain6 -10*Ten


print(f'{TwoThousand} Notes needed of 2000 to represent {Amount} remains->{Remain1}')
print(f'{Fivehundred} Notes needed of 500 to represent {Amount}  remains->{Remain2}')
print(f'{Twohundred} Notes needed of 200 to represent {Amount}  remains->{Remain3}')
print(f'{hundred} Notes needed of 100 to represent {Amount}  remains->{Remain4}')
print(f'{fifty} Notes needed of 50 to represent {Amount}  remains->{Remain5}')
print(f'{Twenty} Notes needed of 20 to represent {Amount}  remains->{Remain6}')
print(f'{Ten} Notes needed of 10 to represent {Amount}  remains->{Remain7}')