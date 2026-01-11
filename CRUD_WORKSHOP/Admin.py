from Emp import Employee
from datastore import Datastore

class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while ch != 6:
            print("1. Add Employee")
            print("2. Search Employee")
            print("3. Show All Employees")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
            ch = int(input("Enter your choice: "))     
            if ch == 1:
                self.addEmp()
            elif ch == 2:
                self.searchEmp()
            elif ch == 3:
                self.showAll()
            elif ch == 4:
                self.updateEmp()
            elif ch == 5:
                self.deleteEmp()
            elif ch == 6:
                print("Exiting...")
            else:
                print("Invalid choice. Please try again.")
        
    def addEmp(self):
        id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        sal = float(input("Enter Employee Salary: "))
        dept = input("Enter Employee Department: ")
        emp = Employee(id, name, sal, dept)
        self.ds.add_employee(emp)
        print("Employee added successfully.")
    
    def showAll(self):
        data = self.ds.showalldata()
        for e in data:
            column = 
    
    def searchEmp(self):
        id = int(input("Enter Employee ID: "))
        res =self.ds.getData

    
    def updateEmp(self):
        id = int(input("Enter Employee ID to update: "))
        res= self.ds.getData(id)
        if res:
            print("note: leave blank to keep current value")
            name = input(f"Enter new name({res[1]}): ") or res[1]
            sal_input = input(f"Enter new salary({res[2]}): ") or str(res[2])
            dept= input(f"Enter new department({res[3]}): ") or res[3]
            emp = Employee(id, name, float(sal_input), dept)
            res= self.ds.updateData(emp)
            print(res)
        else:
            print("Employee not found.")
    
    def deleteEmp(self):
        id = int(input("Enter Employee ID to update: "))
        res= self.ds.getData(id)
        if res:
            if id in self.ds.empdata:
                del self.ds.empdata[id]
                print("Employee deleted successfully.")
        else:
            print("Employee not found.")
                
    
Admin()