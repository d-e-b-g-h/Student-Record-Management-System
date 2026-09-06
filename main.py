import argparse

from student import Student
from manager import StudentManager

from file_handler import (
    load_from_txt,
    save_to_txt,
    load_from_csv,
    save_to_csv,
    load_from_json,
    save_to_json
)


def load_students(filename, file_format):

    if file_format == "txt":
        return load_from_txt(filename)

    elif file_format == "csv":
        return load_from_csv(filename)

    elif file_format == "json":
        return load_from_json(filename)

    else:
        print("Invalid file format.")
        return []


def save_students(filename, file_format, students):

    if file_format == "txt":
        save_to_txt(filename, students)

    elif file_format == "csv":
        save_to_csv(filename, students)

    elif file_format == "json":
        save_to_json(filename, students)

    else:
        print("Invalid file format.")


def show_menu():

    print("\n''''''Student Record Management System ''''''")
    print("1. Display all students")
    print("2. Add new student")
    print("3. Search by Student ID")
    print("4. Search by Name")
    print("5. Search by Department")
    print("6. Search by Average Marks")
    print("7. Update student marks")
    print("8. Remove student")
    print("9. Save records")
    print("10. Exit")


def main():

    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path of the student data file"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"],
        help="Format of the student data file"
    )

    args = parser.parse_args()

    manager = StudentManager()

    students = load_students(args.file, args.format)

    for student in students:
        manager.add_student(student)


    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            manager.display_all_students()


        elif choice == "2":

            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            semester = int(input("Enter Semester: "))

            subject1 = float(input("Enter Subject 1 Marks: "))
            subject2 = float(input("Enter Subject 2 Marks: "))
            subject3 = float(input("Enter Subject 3 Marks: "))

            student = Student(
                student_id,
                name,
                department,
                semester,
                subject1,
                subject2,
                subject3
            )

            manager.add_student(student)

            print("Student added successfully.")


        elif choice == "3":

            student_id = int(input("Enter Student ID: "))

            student = manager.search_student(student_id)

            if student is not None:
                student.display_student()

            else:
                print("Student not found.")


        elif choice == "4":

            name = input("Enter Name: ")

            students = manager.search_by_name(name)

            if len(students) > 0:

                for student in students:
                    student.display_student()

            else:
                print("No student found.")


        elif choice == "5":

            department = input("Enter Department: ")

            students = manager.search_by_department(department)

            if len(students) > 0:

                for student in students:
                    student.display_student()

            else:
                print("No student found.")


        elif choice == "6":

            average_marks = float(
                input("Enter minimum average marks: ")
            )

            students = manager.search_by_average(average_marks)

            if len(students) > 0:

                for student in students:
                    student.display_student()

            else:
                print("No student found.")


        elif choice == "7":

            student_id = int(input("Enter Student ID: "))

            student = manager.search_student(student_id)

            if student is not None:

                subject1 = float(
                    input("Enter new Subject 1 Marks: ")
                )

                subject2 = float(
                    input("Enter new Subject 2 Marks: ")
                )

                subject3 = float(
                    input("Enter new Subject 3 Marks: ")
                )

                student.update_marks(
                    subject1,
                    subject2,
                    subject3
                )

                print("Marks updated successfully.")

            else:
                print("Student not found.")


        elif choice == "8":

            student_id = int(input("Enter Student ID: "))

            removed = manager.remove_student(student_id)

            if removed:
                print("Student removed successfully.")

            else:
                print("Student not found.")


        elif choice == "9":

            save_students(
                args.file,
                args.format,
                manager.students
            )

            print("Records saved successfully.")


        elif choice == "10":

            print("Exiting program.")
            break


        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()