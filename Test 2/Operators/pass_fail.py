# Use logical operators to verify if a student passed (marks > 33 and attendance > 75%)

marks = int(input("Enter the marks of the student(out of 100): "))
attendence = int(input("Enter the attendence of the student(in percentage): "))

 
if marks > 33 and attendence > 75 and marks <= 100:
    print("Student passsed the exam.")
else:
    print("Student Failed.")
