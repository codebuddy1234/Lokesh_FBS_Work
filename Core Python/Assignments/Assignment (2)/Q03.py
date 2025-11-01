# 3. Convert distant given in feet and inches into meter and centimeter. 
FeetInch = float(input("Enter a distance in feet and inches : "))

Meter_dist = FeetInch * 0.3048  # 1feet = 0.3048
Cm_dist =  FeetInch * 30.48     # 1feet = 30.48cm

print(f'Distance in meter of {FeetInch} is {Meter_dist} Meter')
print(f'Distance in Cm of {FeetInch} is {Cm_dist} CentiMeter')
