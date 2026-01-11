from a import A
from b import B

from a import Watch
from b import fitnesstype


class C(A, B):
    def __init__(self):
        print("Constructor of C")
        super().__init__()
    def setData(self):
        print("Set Data from C")
        
class smartwatch(Watch,fitnesstype):
    def __init__(self,brand,watch,type):
        self.brand=brand
        super().__init__(watch,type)
        
watch1=smartwatch("black","y","noise")
print(watch1.__init__())

# c1 = C()
# c1.setData()
