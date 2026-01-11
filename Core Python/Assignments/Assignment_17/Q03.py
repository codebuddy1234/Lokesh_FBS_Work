# Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

from Q01 import Student

class MedicalStudent(Student):
    def __init__(self,sid,sname,age,per,spe,Markintship):
        super().__init__(sid,sname,age,per)
        self.spe=spe
        self.markoint=Markintship
        
    def accept(self):
        super().Accept()
        self.spe=input("Enter SPECIALIZATION: ")
        self.markoint=float(input("Enter MARKS OF INTERNSHIP: "))
        
    def display(self):
        super().Display()
        print(f"SPECILIZATION:{self.spe}\nMARKS OF INTERNSHIP:{self.markoint}")
        
        
    def CalculateRank(self):
        super().CalculateRank()
        avg = (self.per+self.markoint)/2
        if avg > 75:
            return "First Class"
        else:
            return "pass"
        
    def __str__(self):
        super().__str__()
        return f"SPECILIZATION:{self.spe}\nMARKSINT:{self.markoint}"
    
s3=MedicalStudent(4,"kunal",22,70,"ANIMAl",50)
s3.CalculateRank()
s3.display()