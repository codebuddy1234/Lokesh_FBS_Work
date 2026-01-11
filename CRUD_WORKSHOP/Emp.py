class Employee:
    def __init__(self,id,name,sal,dept):
        self.id = id
        self.name = name
        self.sal = sal 
        self.dept = dept 
    def toTuple(self):
        return (self.id,self.name,self.sal,self.dept)
        
if(__name__ == "__main__"):
    emp = Employee(1,'Lokesh',50000,'IT')
    print(emp.toTuple())