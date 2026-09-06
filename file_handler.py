import csv
import json

from student import Student


def load_from_txt(filename):

    students = []

    with open(filename, "r") as file:

        for line in file:

            data = line.strip().split(",")

            if len(data) == 7:

                student = Student(
                    int(data[0].strip()),
                    data[1].strip(),
                    data[2].strip(),
                    int(data[3].strip()),
                    float(data[4].strip()),
                    float(data[5].strip()),
                    float(data[6].strip())
                )

                students.append(student)

    return students


def save_to_txt(filename, students):

    with open(filename, "w") as file:

        for student in students:

            file.write(
                f"{student.student_id}, "
                f"{student.name}, "
                f"{student.department}, "
                f"{student.semester}, "
                f"{student.subject1}, "
                f"{student.subject2}, "
                f"{student.subject3}\n"
            )


def load_from_csv(filename):

    students = []

    with open(filename, "r", newline="") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            student = Student(
                int(row[0]),
                row[1],
                row[2],
                int(row[3]),
                float(row[4]),
                float(row[5]),
                float(row[6])
            )

            students.append(student)

    return students


def save_to_csv(filename, students):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student_ID",
            "Name",
            "Department",
            "Semester",
            "Subject1",
            "Subject2",
            "Subject3"
        ])

        for student in students:

            writer.writerow([
                student.student_id,
                student.name,
                student.department,
                student.semester,
                student.subject1,
                student.subject2,
                student.subject3
            ])


def load_from_json(filename):

    students = []

    with open(filename, "r") as file:

        data = json.load(file)

        for item in data:

            student = Student(
                item["student_id"],
                item["name"],
                item["department"],
                item["semester"],
                item["marks"]["subject1"],
                item["marks"]["subject2"],
                item["marks"]["subject3"]
            )

            students.append(student)

    return students


def save_to_json(filename, students):

    data = []

    for student in students:

        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "department": student.department,
            "semester": student.semester,
            "marks": {
                "subject1": student.subject1,
                "subject2": student.subject2,
                "subject3": student.subject3
            }
        }

        data.append(student_data)

    with open(filename, "w") as file:

        json.dump(data, file, indent=4)