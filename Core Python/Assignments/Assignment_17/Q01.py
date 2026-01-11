# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:
    Rank="PASS"
    def __init__(self,sid,sname,age,per):
        self.sid=sid
        self.sname=sname
        self.age=age
        self.per=per
        
    def Accept(self):
        self.sid= int(input("Enter STUDENT ID: "))
        self.sname= input("Enter STUDENT NAME: ")
        self.age= int(input("Enter AGE:"))
        self.per=float(input("Enter PERCENTAGE: "))
        
    def CalculateRank(self):
        if self.per > 75:
            Student.Rank ="First Class"
        elif self.per > 60:
            Student.Rank= "Second Class"
        elif self.per > 45:
            Student.Rank= "Third Class"
        else:
            Student.Rank="PASS"
            
    def Display(self):
        print(f"SID:{self.sid}\nSTUDENT NAME:{self.sname}\nAGE:{self.age}\nPERCENTAGE:{self.per}\nStudent Rank:{Student.Rank}")
        
    def __str__(self):
        data = f"SID:{self.sid}\nSTUDENT NAME:{self.sname}\nAGE:{self.age}\nPERCENTAGE:{self.per}\nSTUDENT RANK:{Student.Rank}"
        return data

s1=Student(1,"Lokesh",20,80)
s1.CalculateRank()
s1.Display()

s2=Student(0,"",0,0)
s2.Accept()
s2.CalculateRank()
print(s2)
        
        