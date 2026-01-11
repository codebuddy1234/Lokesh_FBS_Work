class A:
    def __init__(self):
        print("Constructor of A")
        
    def getDATA(self):
        print("Data from A")
        
    def setData(self):
        print("Set Data from A")
        
class Watch:
    def __init__(self,watch):
        self.watch=watch
        super.__init__()
        