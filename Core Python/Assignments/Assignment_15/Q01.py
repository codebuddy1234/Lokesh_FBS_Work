# Create a class Book with members as bid,bname,price and author.Add following # methods: 
# # a. Constructor (Support both parameterized and parameterless) 
# # b. Destructor 
# # c. ShowBook

class Book:
    def __init__(self, bid=1, bname="Trading", price=1000, author="Lokesh"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        
    def ShowBook(self):
        print(f"BID: {self.bid}")
        print(f"BNAME: {self.bname}")
        print(f"PRICE: {self.price}")
        print(f"AUTHOR: {self.author}")
        print("-" * 20)
        
    def __del__(self):
        print("Book object destroyed")
        
b1 = Book(2, "Forex TRading", 1500, "Kunal Nikam")
b1.ShowBook()
