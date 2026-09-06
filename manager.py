class StudentManager:

    def __init__(self):
        self.students = []


    def add_student(self, student):
        self.students.append(student)


    def display_all_students(self):
        if len(self.students) == 0:
            print("No student records found.")
        else:
            for student in self.students:
                student.display_student()


    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None


    def search_by_name(self, name):
        result = []

        for student in self.students:
            if student.name.lower() == name.lower():
                result.append(student)

        return result


    def search_by_department(self, department):
        result = []

        for student in self.students:
            if student.department.lower() == department.lower():
                result.append(student)

        return result


    def search_by_average(self, average_marks):
        result = []

        for student in self.students:
            if student.calculate_average() > average_marks:
                result.append(student)

        return result


    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True

        return False