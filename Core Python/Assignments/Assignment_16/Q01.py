# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count=0
    def __init__(self,bid=1,bname="RICH",price=500,author="Lokesh"):
        Book.count +=1
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        
    def ShowBook(self):
        Data = f'BOOKID:{self.bid}\nBOOKNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}\nBOOKCOUNT:{Book.count}'
        return Data
    
    def __del__(self):
        print("DESTROYED!!!!!!!")
        
b1=Book(2,"POOR",200,"kunal")
print(b1.ShowBook())

b2=Book()
print(b2.ShowBook())
        
