# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self,sid=1,sname="white",type="formal",price=500,size="large"):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
        
    def ShowShirt(self):
        print("SID:",self.sid)
        print("SNAME:",self.sname)
        print("TYPE:",self.type)
        print("PRICE:",self.price)
        print("SIZE:",self.size)
        print("*"*50)
        
    def __del__(self):
        print("DESTROYED!!!!!!!!!!!")
        
s1=Shirt(2,"BLACK COTTON","form",800,"M")
s1.ShowShirt()