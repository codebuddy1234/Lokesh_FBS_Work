# Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

from Q01 import Student


class EnggStudent(Student):
    def __init__(self,sid,sname,age,per,branch,intmarks):
        super().__init__(sid,sname,age,per)
        self.branch=branch
        self.intmarks=intmarks
        
    def accept(self):
        super().Accept()
        self.branch=input("Enter Your BRANCH: ")
        self.intmarks=int(input("Enter INTMARKS: "))
        
    def display(self):
        super().Display()
        print(f"BRANCH:{self.branch}\nINTMARKS:{self.intmarks}")
        
    def CalculateRank(self):
        avg = (self.per+self.intmarks)/2
        if avg > 75:
            return "First Class"
        elif avg > 60:
            return "Second class"
        elif avg >45:
            return "Third Class"
        else :
            return "pass"
    
    def __str__(self):
        return f"SID:{self.sid}\nSNAME:{self.sname}\nAGE:{self.age}\nPERCENTAGE:{self.per}\nBRANCH:{self.branch}\nRANK:Calculaterank()\n"
    
s3=EnggStudent(3,"ka",20,80,"AIML",60)
s3.CalculateRank()
s3.display()
    