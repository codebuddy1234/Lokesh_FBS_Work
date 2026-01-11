class Organism:
    def __init__(self,type="living"):
        self.__type=type  #__type : private variable (encapsulation)
        
    def getData(self):
        return self.__type
    
class Animal(Organism):
    def __init__(self,type,name):
        self.name=name
        super().__init__(type)
        
class Dog(Animal):
    def __init__(self,type,name,voice):
        super().__init__(type,name)
        self.voice=voice
        
    def getdetails(self):
        return (f"TYPE:{self.getData()}\nNAME:{self.name}\nVOICE:{self.voice}")
    
obj1=Dog("Living","JACKY","BARKING")
print(obj1.getdetails())
print(Dog.mro())