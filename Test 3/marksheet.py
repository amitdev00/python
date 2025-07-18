student_name = str(input("Enter name of the student: "))

eng = int(input("Enter the marks in english: "))
maths = int(input("Enter the marks in maths: "))
physics = int(input("Enter the marks in physics: "))
chemistry = int(input("Enter the marks in chemistry: "))
computer = int(input("Enter the marks in computer science: "))
hindi = int(input("Enter the marks in hindi: "))


print("--------------------Student Report----------------------")
print(f"Name:- {student_name}")

def get_grade(marks):
    if 100 >=  marks >= 86:
        return "A"
    elif 85 >= marks >= 71:
        return "B"
    elif 70 >= marks >= 61:
        return "C"
    elif 60 >= marks >= 51:
        return "D"
    elif 50 >= marks >= 41:
        return "E"
    elif marks <= 40:
        return "F"


print("Subject Name                 Marks Obtained        Subject Grades")
print(f"English                         {eng}                     {get_grade(eng)}")
print(f"Maths                           {maths}                     {get_grade(maths)}")
print(f"Physics                         {physics}                     {get_grade(physics)}")
print(f"Chemistry                       {chemistry}                     {get_grade(chemistry)}")
print(f"Computer Science                {computer}                     {get_grade(computer)}")
print(f"Hindi                           {hindi}                     {get_grade(hindi)}")
print("---------------------------------------------------------------------")


total_marks = (eng + maths + physics + chemistry + computer + hindi)
print(f"Total Marks:-                   {total_marks}") 
print(" ")

if 100 >= total_marks >= 1:
    print("Grade:-                          F")
elif 200 >= total_marks >= 101:
    print("Grade:-                          E")
elif 300 >= total_marks >= 201:
    print("Grade:-                          D")
elif 400 >= total_marks >= 301:
    print("Grade:-                          C")
elif 500 >= total_marks >= 401:
    print("Grade:-                          B")
elif 600 == total_marks >= 501:
    print("Grade:-                          A")

percentage = (total_marks / 600) * 100
print(f"Percentage:-                     {round(percentage,2)}%")

if percentage >= 71:
    print("Division in class:-              First")
elif 70 > percentage >= 61:
    print("Division in class:-              Second")
elif 60 > percentage >= 51:
    print("Division in class:-              Third")
elif 50 > percentage >= 41:
    print("Division in class:-              Fourth")
else:
    print("Division in class:-              No Division")


if eng <33 or maths<33 or physics<33 or chemistry<33 or computer<33 or hindi < 33:
    print("Status:-                         Fail")
else:
    print("Status:-                         Pass")
