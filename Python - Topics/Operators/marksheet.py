marks_english = 78
marks_science = 45
marks_maths = 90

total_marks = marks_english + marks_maths + marks_science
print("Total Marks: ", total_marks)

average = total_marks / 300
marks_percentage = average * 100
print(f"Percentage is {marks_percentage}%")

if marks_percentage >= 80:
    print("Grade A+")
elif marks_percentage < 80 and marks_percentage >=70:
    print("Grade A")
elif marks_percentage < 70 and marks_percentage >= 60:
    print("Grade B")
elif marks_percentage < 60 and marks_percentage >= 50:
    print("Grade C")
else:
    print("Fail")
