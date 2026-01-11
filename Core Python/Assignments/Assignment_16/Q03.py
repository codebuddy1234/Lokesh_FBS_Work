# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:
    P_size=100
    count=0
    def __init__(self,sid=1,sname="plane",type="formal",price=1000,size="L"):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        Shirt.count +=1
        
    def Apply_p(self):
        if self.size =="S":
            self.price=self.price
        elif(self.size=="M"):
            self.price += Shirt.P_size
        elif(self.size=="L"):
            self.price += (2*Shirt.P_size)
        else:
            self.price += (3*Shirt.P_size)
                
    def ShowShirt(self):
        print(f"SID:{self.sid}\nSNAME:{self.sname}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}\nCOUNT:{Shirt.count}")
        
s1=Shirt()
s1.Apply_p()
s1.ShowShirt()      

s2=Shirt(2,"checkstype","Fancy",800,"XL")
s2.Apply_p()
s2.ShowShirt()  
        