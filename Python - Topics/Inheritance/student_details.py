# Create Person as a base class and student as derived class, 
# Student has id and name as parameter, 
# and student has course and grade, 
# call all the details of students.

class Person: 
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Student(Person):
    def __init__(self, id, name, course, grade):
        super().__init__(id, name)
        self.course = course
        self.grade = grade
    
    def details(self):
        return f"ID :- {self.id}\nName :- {self.name}\nCourse :- {self.course}\nGrade :- {self.grade}"
    
obj_student = Student(1, "Amit", "BCA", "O++")
print(obj_student.details())



