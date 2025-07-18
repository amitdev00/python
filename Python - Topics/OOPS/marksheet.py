# make a marksheet of student
# find percentage of student
# also give grades
# if marks < 35 then fail the student


class Marksheet:
    def __init__(self, name, eng, science, maths, max_marks):
        self.name = name
        self.eng = eng
        self.science = science
        self.maths = maths
        self.max_marks = 300

    def calculate_marks(self):
        return self.eng + self.science + self.maths

    def calculate_percentage(self):
        return ((self.eng + self.science + self.maths) / self.max_marks) * 100

    def calculate_grade(self):
        while self.eng and self.maths and self.science > 33:
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
                print("Student Failed.")
                break
        print("Marks in every subject should be above 35.")
        print("Student Failed.")


name = str(input("Enter the name: "))
eng = int(input("Enter the marks in english: "))
science = int(input("Enter the marks in science: "))
maths = int(input("Enter the marks in maths: "))
max_marks = 300

obj_marksheet = Marksheet(name, eng, maths, science, max_marks)

marks = obj_marksheet.calculate_marks()
marks_percentage = obj_marksheet.calculate_percentage()
grade = obj_marksheet.calculate_grade()

print(f"Name: {name}")
print(f"Marks: {marks} / {max_marks}")
print(f"Percentage: {marks_percentage}%")
print(f"Grade: {grade}")
