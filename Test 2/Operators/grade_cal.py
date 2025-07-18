# Implement a simple grade calculator using assignment and comparison.
max_marks = 500
eng = int(input("Enter the marks in english(out of 100): ")) 
physics =int(input("Enter the marks in physics(out of 100): "))  
maths = int(input("Enter the marks in maths(out of 100): "))
chemistry = int(input("Enter the makrs in chemistry(out of 100): "))
computer_science = int(input("Enter the marks in computer science(out of 100): "))

total_marks = eng + physics + maths + chemistry + computer_science
average = total_marks / max_marks
percentage = average * 100

print(f"Total mark of the student is: {total_marks} / {max_marks}")
print(f"Perentage of student is: {round(percentage)}%")

while eng and physics and maths and chemistry and computer_science > 33:

    if percentage > 95:
        print("Grade A++")  
    elif 95 > percentage >= 90:
        print("Grade A+")
    elif 90 > percentage > 85:
        print("Grade A")
    elif 85 > percentage > 80:
        print("Grade B++")
    elif 85 > percentage > 80:
        print("Grade B+")
    elif 80 > percentage > 75:
        print("Grade B")
    elif 75 > percentage > 70:
        print("Grade C++")
    elif 70 > percentage > 65:
        print("Grade C+")
    elif 65 > percentage > 60:
        print("Grade C")
    elif 60 > percentage > 35:
        print("Grade D")
    else:
        print("Student Failed.")
    break
print("Marks in every subject should be 33 or above.")
print("Student Failed.")
