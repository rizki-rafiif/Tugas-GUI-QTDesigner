# cara import
from Person import Person

class Student(Person) :
   def __init__(self, fname, lname):
    super().__init__(fname, lname)

student = Student("Bagus", "Bayu")

print(student.printname())