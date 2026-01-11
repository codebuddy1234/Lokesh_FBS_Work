# Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method


class Student:
    def __init__(self, sid, name, branch):
        self.sid = sid
        self.name = name
        self.branch = branch

    def __str__(self):
        return f"ID:{self.sid}, Name:{self.name}, Branch:{self.branch}"

    
class College:
    def __init__(self, college_name, max_students):
        self.college_name = college_name
        self.max_students = max_students
        self.students = []   # collection of students

    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("College is full")

    def getStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                return s
        return "Student not found"

    def removeStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                self.students.remove(s)
                print("Student removed")
                return
        print("Student not found")

    def __str__(self):
        result = f"College: {self.college_name}\nStudents:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result

c1 = College("ABC College", 2)

s1 = Student(1, "Lokesh", "CSE")
s2 = Student(2, "Kunal", "ENTC")

c1.addStudent(s1)
c1.addStudent(s2)

print(c1)

print(c1.getStudent(1))

c1.removeStudent(2)
print(c1)
