class Vehicle:
    def __init__(self,brand="BMW",color="WHITE",price="8000000"):
        self.brand =brand 
        self.color= color
        self.price=price
    def getData(self):
        print(f'BRAND:{self.brand}')
        print(f'COLOR:{self.color}')
        print(f'PRICE:{self.price}')

class Car(Vehicle):
    def __init__(self,b,c,p,sunroof):
        super().__init__(b,c,p)
        self.sunroof=sunroof
        
    def getData(self):
        super().getData()
        print("SUNROOF:",self.sunroof)
        
car1=Car("audi","black",10000,"yes")
car1.getData()
