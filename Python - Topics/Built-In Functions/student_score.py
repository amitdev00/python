# Write a function that asks the user to input the names and marks of student.
# Inside the function: 
# Store data in a dictionary.
# Calculate and print the total, average (rounded to 2 decimal places), highest, and lowest marks.
# Check if student passed (marks ≥ 35). Print all results.

def student_report():
    student_name = str(input("Enter the name of the student: "))
    eng = int(input("Enter the marks in english: "))
    maths = int(input("Enter the marks in mathematics: "))
    science = int(input("Enter the marks in science: "))

    student_details = {
        "name" : student_name,
        "marks" : {
            "english" : eng,
            "maths" : maths,
            "science" : science
        }
    }

    max_marks = 300
    total_marks = eng + maths + science
    print(f"Total marks obtained by the {student_name} is {total_marks}")

    average = round(total_marks / 3)
    print(f"Average marks of the {student_name} is: {average}")

    highest_score = max(student_details["marks"])
    print(f"Highest score of the student is: {highest_score}")

    lowest_score = min(student_details["marks"])
    print(f"Minimum score of the student is: {lowest_score}")

    if eng and maths and science > 35:
        print(f"{student_name} passed the exam.")
    else:
        print(f"{student_name} failed the exam.")

    return student_details

y = student_report()
print(y)