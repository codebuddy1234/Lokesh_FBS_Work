from config import storage
import mysql.connector

class Datastore:
    def __init__(self):
        if(storage == 'dictionary'):
        self.empdata = {}
        
        
    def add_employee(self, emp):
        self.empdata[emp.id] = emp.toTuple()
        
    def showalldata(self):
        return self.empdata
    
    def getData(self, emp_id):
        if emp_id in self.empdata:
            return self.empdata[emp_id]
        else:
            return None
        
    def updateData(self, emp):
        if emp.id in self.empdata:
            self.empdata[emp.id] = emp.toTuple()
            return True
        else:
            return False
        
    def deleteData(self, emp_id):
        self.empdata.pop(emp_id, None)
    
    def connectDB(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Lokesh@123",
                database="employeedb"  
                
        except mysql.connector.errors.ProgramingError as e:
            if("Unknown Database" in e.msg.lower()):
                conn
            else:
                print("Other ERROR")
        except:
            print("SOMETHING Wrong")
    
if(__name__ == "__main__"):
    from Emp import Employee
    emp = Employee(1, 'Lokesh', 50000, 'IT')
    ds = Datastore()
    ds.add_employee(emp)
    print(ds.showalldata())