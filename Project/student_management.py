# student management system
# name
# grade
# marks
# return all the values
# add new student
# updated list
# updated student 
# updated list
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def show_details(self):
        return f"   {self.id}             {self.name}       "
    
class Marks(Student):
    def __init__(self,id, name, eng, maths, physics, chemistry, computer ):
        super().__init__(self, id, name)
        self.eng = eng
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.computer = computer

    def show_details(self):
        return f"{self.eng}\nMaths :- {self.maths}\nPhysics :- {self.physics}\nChemistry :- {self.chemistry}\nComputer Science :- {self.computer}"

class Grade(Marks):
    def __init__(self, eng, maths, physics, chemistry, computer):
        super().__init__( eng, maths, physics, chemistry, computer)

    def calculate_total_marks(self):
        return self.eng + self.maths + self.physics + self.chemistry + self.computer
    
    def calculate_percentage(self):
        return (self.calculate_total_marks() / 500) * 100
    
    def caluculate_grade(self):
        while (self.eng and self.maths and self.physics and self.chemistry and self.computer) < 33:
            return "Marks should be above 33 in every subject.\nStudent failed."
        else:
            while 101 < (self.eng and self.maths and self.physics and self.chemistry and self.computer) >= 33:
                if self.calculate_percentage() > 95:
                    return "A++"  
                elif 95 > self.calculate_percentage() >= 90:
                    return "A+"
                elif 90 > self.calculate_percentage() > 85:
                    return "A"
                elif 85 > self.calculate_percentage() > 80:
                    return "B++"
                elif 85 > self.calculate_percentage() > 80:
                    return "B+"
                elif 80 > self.calculate_percentage() > 75:
                    return "B"
                elif 75 > self.calculate_percentage() > 70:
                    return "C++"
                elif 70 > self.calculate_percentage() > 65:
                    return "C+"
                elif 65 > self.calculate_percentage() > 60:
                    return "C"
                elif 60 > self.calculate_percentage() > 35:
                    return "D"
                else:
                    return "Student Failed."
   
   
ID = int(input("Enter the Student ID :- "))
name = str(input("Enter your name :- "))
english_marks = int(input("Enter marks in english :- "))
math_marks = int(input("Enter marks in maths :- "))
physics_marks = int(input("Enter marks in physics :- "))
chemistry_marks = int(input("Enter marks in chemistry :- "))
computer_marks = int(input("Enter marks in computer science :- "))

print("-------------------Student Report-------------------")
print("Student ID       Name   ")
obj_student = Student(ID, name)
print(obj_student.show_details())

obj_marks = Marks(english_marks, math_marks, physics_marks, chemistry_marks, computer_marks)
print(obj_marks.show_details())

obj_grade = Grade(english_marks, math_marks, physics_marks, chemistry_marks, computer_marks)
print(f"Marks Obtained :- {obj_grade.calculate_total_marks()} / 500")
print(f"Percentage Obtained :- {obj_grade.calculate_percentage()}%")
print(f"Grade :- {obj_grade.caluculate_grade()}")
