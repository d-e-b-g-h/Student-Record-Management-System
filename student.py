class Student:

    def __init__(self, student_id, name, department, semester, subject1, subject2, subject3):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3


    def calculate_total(self):
        total = self.subject1 + self.subject2 + self.subject3
        return total


    def calculate_average(self):
        average = self.calculate_total() / 3
        return average


    def get_result(self):
        if self.subject1 >= 40 and self.subject2 >= 40 and self.subject3 >= 40:
            return "Pass"
        else:
            return "Fail"


    def update_marks(self, subject1, subject2, subject3):
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3


    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)
        print("Subject 1 Marks:", self.subject1)
        print("Subject 2 Marks:", self.subject2)
        print("Subject 3 Marks:", self.subject3)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())
        print("Result:", self.get_result())
        print("-" * 40)