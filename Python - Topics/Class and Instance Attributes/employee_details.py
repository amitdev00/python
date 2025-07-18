class Employee:
    empCount = 0
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        Employee.empCount += 1
        print(f"Name:- {self.name}")
        print(f"Department:- {self.dept}")
        print(f"Employee Number:- {Employee.empCount}")
        print("")

e1 = Employee("Amit", "Trainee")
e2 = Employee("Suryansh", "Trainee")
e3 = Employee("Damanpreet kaur", "Trainer")


