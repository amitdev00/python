class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Marks(Student):
    def __init__(self, id, name, eng, maths, physics, chemistry, computer):
        super().__init__(id, name)
        self.eng = eng
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.computer = computer

    def calculate_total_marks(self):
        return self.eng + self.maths + self.physics + self.chemistry + self.computer
    
    def calculate_percentage(self):
        return (self.calculate_total_marks() / 500) * 100
    
class Grade(Marks):
    def __init__(self, id, name, eng, maths, physics, chemistry, computer):
        super().__init__(id, name, eng, maths, physics, chemistry, computer)

    def calculate_grade(self):
        if any(mark < 33 for mark in [self.eng, self.maths, self.physics, self.chemistry, self.computer]):
            return ("Marks should be above 33 in every subject"
                    "Student Failed.")
        
        percentage = self.calculate_percentage()

        while True:
            if percentage >=93: 
                return ("A")
            elif percentage  >=90 and percentage <= 93:
                return ("-A")
            elif percentage >= 87 and percentage <= 90:
                return("B+")
            elif percentage >=83 and percentage >= 87:
                return ("B")
            elif percentage >= 80 and percentage >= 83:
                return ("B-")
            elif percentage >= 77 and percentage >= 80:
                return ("C+")
            elif percentage >= 73 and percentage >= 77:
                return ("C")
            elif percentage >= 70 and percentage >= 73:
                return ("C-")
            elif percentage >= 67 and percentage >= 70:
                return  ("D+")
            elif percentage >= 63 and percentage >= 67:
                return ("D")
            elif percentage >= 60 and percentage >= 63:
                return ("D-")
            else:
                return ("F")
            
class ManageStudent(Grade):
    def __init__(self, id, name, eng, maths, physics, chemistry, computer):
        super().__init__(id, name, eng, maths, physics, chemistry, computer)

    def add_student(self):
        student_dict = {}

        id = int(input("Enter Student ID: "))
        if self.id in student_dict:
            return f"Student ID already exists."

        name = str(input("Enter name of the student: "))
        eng = int(input("Enter marks in english: "))
        maths = int(input("Enter marks in mathematics: "))
        physics = int(input("Enter marks in physics: "))
        chemistry = int(input("Enter marks in chemistry: "))
        computer = int(input("Enter marks in computer: "))

        student_info = Grade(id, name, eng, maths, physics, chemistry, computer)
        self.student_dict[id] = student_info


    def update_student(self):
        id = int(input("Enter the Student ID whose data you want to update: "))

        if id not in self.student_dict:
            print("Student ID not found. Please add the student first or check the ID.\n")
            return

        student = self.student_dict[id]

        print(f"\nYou are updating details for student: {student.name}")
        print("If you want to keep a value unchanged, just press Enter.\n")

        new_name = input(f"Enter new name (Current: {student.name}): ")
        if new_name.strip() == "":
            new_name = student.name

        new_eng = input(f"Enter new English marks (Current: {student.eng}): ")
        if new_eng.strip() == "":
            new_eng = student.eng
        else:
            new_eng = int(new_eng)

        new_maths = input(f"Enter new Mathematics marks (Current: {student.maths}): ")
        if new_maths.strip() == "":
            new_maths = student.maths
        else:
            new_maths = int(new_maths)

        new_physics = input(f"Enter new Physics marks (Current: {student.physics}): ")
        if new_physics.strip() == "":
            new_physics = student.physics
        else:
            new_physics = int(new_physics)

        new_chemistry = input(f"Enter new Chemistry marks (Current: {student.chemistry}): ")
        if new_chemistry.strip() == "":
            new_chemistry = student.chemistry
        else:
            new_chemistry = int(new_chemistry)

        new_computer = input(f"Enter new Computer marks (Current: {student.computer}): ")
        if new_computer.strip() == "":
            new_computer = student.computer
        else:
            new_computer = int(new_computer)

        updated_student = Grade(id, new_name, new_eng, new_maths, new_physics, new_chemistry, new_computer)

        self.student_dict[id] = updated_student

        print("\nStudent record has been successfully updated!\n")
                
    def show_all_students(self):
        if not self.student_dict:
            print("⚠ No student records found.\n")
            return

        print("\n📋 All Student Records:\n")
        print("-" * 50)

        for student_id, student in self.student_dict.items():
            print(f"Student ID   : {student.id}")
            print(f"Name         : {student.name}")
            print(f"English      : {student.eng}")
            print(f"Mathematics  : {student.maths}")
            print(f"Physics      : {student.physics}")
            print(f"Chemistry    : {student.chemistry}")
            print(f"Computer     : {student.computer}")
            print(f"Percentage   : {student.calculate_percentage():.2f}%")
            print("-" * 50)


manager = ManageStudent(id)
manager.add_student()
manager.add_student()
manager.show_all_students()