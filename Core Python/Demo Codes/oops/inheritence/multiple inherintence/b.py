class B:
    def __init__(self):
        print("Constructor of B")
        
    def showDATA(self):
        print("Data from B")
        
    def setData(self):
        print("Set Data from B")
        
        
class fitnesstype:
    def __init__(self,type,watch):
        self.type=type
        super().__init__(watch)