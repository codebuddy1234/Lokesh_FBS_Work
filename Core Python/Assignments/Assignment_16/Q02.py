# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount=0.2
    def __init__(self,pid=1,pname="MacBook",price=50000,quantity=20):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        
    def Dis_price(self):
        self.price = self.price - (self.price*Product.discount)
        
        
    def ShowProduct(self):
        print(f'PID:{self.pid}\nPRODUCT:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}')
        
p1=Product()
p1.Dis_price()
p1.ShowProduct()
        
p2=Product(2,"DELL Laptop",40000,80)
p2.Dis_price()
p2.ShowProduct()