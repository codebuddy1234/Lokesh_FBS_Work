# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self,pid=1,pname="MANGO",price=100,quantity=50):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        
    def ShowProduct(self):
        print("PID:",self.pid)
        print("PNAME:",self.pname)
        print("PRICE:",self.price)
        print("QUANTITY:",self.quantity)
        print("*"*50)
        
    def __del__(self):
        print("DESTROYED!!!!!!!!!!!")
        
p1=Product(2,"APPLE",200,100)
p1.ShowProduct()