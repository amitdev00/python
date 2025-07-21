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
        return f"Student Id :- {self.id}\nName :- {self.name}"
    
class Marks(Student):
    def __init__(self,id, name, eng, maths, physics, chemistry, computer):
        super().__init__(id, name)
        self.eng = eng
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.computer = computer

    def show_details(self):
        return f"ID :- {self.id}\nName :- {self.name}\nEnglish :- {self.eng}\nMaths :- {self.maths}\nPhysics :- {self.physics}\nChemistry :- {self.chemistry}\nComputer Science :- {self.computer}"

class Grade(Marks):
    def __init__(self,id, name, eng, maths, physics, chemistry, computer):
        super().__init__(id, name, eng, maths, physics, chemistry, computer)

    # def show_details(self):
    #     return f"Student ID :- {self.id}\nName :- {self.name}\nEnglish :- {self.eng}\nMaths :- {self.maths}\nPhysics :- {self.physics}\nChemistry :- {self.chemistry}\nComputer Science :- {self.computer}"

    def calculate_total_marks(self):
        return self.eng + self.maths + self.physics + self.chemistry + self.computer
    
    def calculate_percentage(self):
        return (self.calculate_total_marks() / 500) * 100
    
    def calculate_grade(self):
        if any(mark < 33 for mark in [self.eng, self.maths, self.physics, self.chemistry, self.computer]):
            return "Marks should be above 33 in every subject.\nStudent failed."
                
        if self.calculate_percentage() > 97:
            return "A++"  
        elif 97 > self.calculate_percentage() >= 95:
            return "A+"
        elif 95 > self.calculate_percentage() > 90:
            return "A"
        elif 90 > self.calculate_percentage() > 85:
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
                
class ManageStudent:
    def __init__(self):
        self.student_dict = {}

    def add_new_student(self):
        id = int(input("Enter Student ID :- "))
        name = input("Enter Student Name :- ")
        eng = int(input("Enter marks in English :- "))
        maths = int(input("Enter marks in Maths :- "))
        physics = int(input("Enter marks in Physics :- "))
        chemistry = int(input("Enter marks in Chemistry :- "))
        computer = int(input("Enter marks in Computer :- "))

        new_student = Grade(id, name, eng, maths, physics, chemistry, computer)
        self.student_dict[id] = new_student
        print(f"\n{name} added successfully.\n")

    def update_student(self):
        id = int("Enter the Student ID: ")
        if id in self.student_dict:
            print("Current Details: ")
            print(self.student_dict[id].show_details())
            print("\nEnter new details (leave blank to keep current value): ")

            name = input("Enter new name: ")
            eng = int(input("Enter new english marks: "))
            maths = int(input("Enter new maths marks: "))
            physics = int(input("Enter new physics marks: "))
            chemistry = int(input("Enter new chemistry marks: "))
            computer = int(input("Enter new computer marks: "))

            student = self.student_dict[id]
            if name:
                student.name = name
            if eng:
                student.eng = int(eng)
            if maths:
                student.maths = int(maths)
            if physics:
                student.physics = int(physics)
            if chemistry:
                student.chemistry = int(chemistry)
            if computer:
                student.computer = int(computer)

            print("Student details updated successfully.\n")
        else:
            print("Student ID not found.\n")


    def display_all_students(self):
        print("\n---------------- All Students Report ----------------")
        if not self.student_dict:
            print("No students found.")
            return
        for student in self.student_dict.values():
            print(student.show_details())
            print(f"Total Marks: {student.calculate_total_marks()} / 500")
            print(f"Percentage: {student.calculate_percentage():.2f}%")
            print(f"Grade: {student.calculate_grade()}")
            print("--------------------------------------------------")
            

manager = ManageStudent()

while True:
    print("\n1. Add New Student")
    print("2. Show All Students")
    print("3. Exit")
    option = input("Choose Option :-  (1/2/3/4): ")

    if option == "1":
        manager.add_new_student()
    elif option == "2":
        manager.update_student()
    elif option == "3":
        manager.display_all_students()
    elif option == "4":
        print("Exit")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
   
# ID = int(input("Enter the Student ID :- "))
# name = str(input("Enter your name :- "))
# english_marks = int(input("Enter marks in english :- "))
# math_marks = int(input("Enter marks in maths :- "))
# physics_marks = int(input("Enter marks in physics :- "))
# chemistry_marks = int(input("Enter marks in chemistry :- "))
# computer_marks = int(input("Enter marks in computer science :- "))

# print("-------------------Student Report-------------------")
# obj_student = Student(ID, name)
# print(obj_student.show_details())

# obj_grade = Grade(ID, name, english_marks, math_marks, physics_marks, chemistry_marks, computer_marks)
# print(f"{obj_grade.show_details()}")
# print(f"Marks Obtained :- {obj_grade.calculate_total_marks()} / 500")
# print(f"Percentage Obtained :- {obj_grade.calculate_percentage()}%")
# print(f"Grade :- {obj_grade.calculate_grade()}")

obj_manage_student = ManageStudent()
# obj_manage_student.student_dict[ID] = obj_grade
obj_manage_student.display_all_students()


