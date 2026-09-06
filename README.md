# Student Record Management and Search System

A Python-based Student Record Management and Search System developed using Object-Oriented Programming, modular programming, file handling, command-line arguments, and basic searching techniques.

## Objective

The objective of this project is to develop a Student Record Management and Search System using Python.

The system is designed to manage student information such as Student ID, Name, Department, Semester, and marks in three subjects.

This project demonstrates the practical implementation of:

* Object-Oriented Programming
* Classes and Objects
* Constructors
* Attributes
* Instance Methods
* Modular Programming
* File Handling
* TXT File Handling
* CSV File Handling
* JSON File Handling
* Command-Line Arguments
* Basic Searching
* Conditional Searching
* Loops and Conditions

The program allows users to manage student records through a menu-driven interface.

The system supports storing and loading student records using three different file formats:

* TXT
* CSV
* JSON

## Features

The Student Record Management System provides the following features:

1. Display all student records
2. Add a new student
3. Search by Student ID
4. Search by Name
5. Search by Department
6. Search by Average Marks
7. Update student marks
8. Remove a student
9. Save student records
10. Exit the program

Additional features include:

* Calculation of total marks
* Calculation of average marks
* Pass or Fail result evaluation
* TXT file support
* CSV file support
* JSON file support
* Command-line arguments
* Modular project structure
* Object-Oriented Programming

The project has been tested using multiple student records.

## Project Structure

student-record-system/
│
├── main.py
├── student.py
├── manager.py
├── file_handler.py
│
├── data/
│   ├── students.txt
│   ├── students.csv
│   └── students.json
│
└── README.md

The project is divided into separate Python modules so that each file has a specific responsibility.

# Technologies Used

The project is developed using:

* Python 3
* Visual Studio Code
* Terminal / Command Line
* Git
* GitHub

# Python Modules Used

The project uses Python built-in modules only.

## csv

The `csv` module is used for reading and writing CSV files.

Examples:

csv.reader()
csv.writer()

## json

The `json` module is used for reading and writing JSON files.

Examples:

json.load()
json.dump()

## argparse

The `argparse` module is used to accept command-line arguments.

It allows the user to specify:

* File path
* File format

Example:

  python3 main.py --file data/students.csv --format csv

No external libraries such as Pandas or NumPy are required.

# Description of Each File

## main.py

`main.py` is the main entry point of the program.

It is responsible for:

* Processing command-line arguments
* Loading student records
* Creating the StudentManager object
* Displaying the menu
* Taking user input
* Performing selected operations
* Saving records
* Controlling the overall program flow

## student.py

This file contains the `Student` class.

The Student class represents an individual student.

It stores:

* Student ID
* Name
* Department
* Semester
* Subject 1 Marks
* Subject 2 Marks
* Subject 3 Marks

It also performs operations such as:

* Calculating total marks
* Calculating average marks
* Determining Pass or Fail
* Updating marks
* Displaying student information

Main methods include:

calculate_total()
calculate_average()
get_result()
update_marks()
display_student()

## manager.py

This file contains the `StudentManager` class.

The StudentManager is responsible for managing multiple Student objects.

The students are stored in a list.

Main operations include:

* Adding students
* Displaying all students
* Searching by Student ID
* Searching by Name
* Searching by Department
* Searching by Average Marks
* Removing students

Main methods include:

add_student()
display_all_students()
search_student()
search_by_name()
search_by_department()
search_by_average()
remove_student()

## file_handler.py

This file handles all file-related operations.

It contains functions for loading and saving student records.

### TXT File Functions

load_from_txt()
save_to_txt()

### CSV File Functions

load_from_csv()
save_to_csv()

### JSON File Functions

load_from_json()
save_to_json()

When loading data, the file handler converts records into Student objects.

When saving data, Student objects are converted into the appropriate file format.

# Object-Oriented Programming Concepts Used

Object-Oriented Programming is one of the main concepts used in this project.

## Classes

A class is a blueprint used to create objects.

This project uses two main classes:

Student
StudentManager

The `Student` class represents an individual student.

The `StudentManager` class manages multiple Student objects.

## Objects

An object is an instance of a class.

Each student record in this project is represented by a Student object.

For example:

student = Student(
    student_id,
    name,
    department,
    semester,
    subject1,
    subject2,
    subject3
)

This creates a Student object containing the information of one student.

## Constructor

The constructor is the `__init__()` method.

It initializes the attributes of a Student object when a new student is created.

The constructor stores:

student_id
name
department
semester
subject1
subject2
subject3

## Attributes

Attributes are variables that store information related to an object.

The Student class contains attributes such as:

student_id
name
department
semester
subject1
subject2
subject3

## Instance Methods

Instance methods perform operations related to a particular object.

The Student class uses methods such as:

calculate_total()
calculate_average()
get_result()
update_marks()
display_student()

These methods work using the information stored inside each Student object.

# How the Student Class Works

The Student class represents one student record.

Conceptually:

Student
   │
   ├── Student ID
   ├── Name
   ├── Department
   ├── Semester
   ├── Subject 1 Marks
   ├── Subject 2 Marks
   └── Subject 3 Marks

The marks are used to calculate the total and average.

Subject 1
    │
Subject 2
    │
Subject 3
    │
    ▼
Total Marks
    │
    ▼
Average Marks
    │
    ▼
Pass / Fail Result

# Total Marks Calculation

The total marks are calculated by adding the marks of all three subjects.

Formula:

Total Marks = Subject 1 + Subject 2 + Subject 3

Example:

Subject 1 = 78
Subject 2 = 82
Subject 3 = 69

Total Marks = 78 + 82 + 69
Total Marks = 229

# Average Marks Calculation

The average marks are calculated using:

Average Marks = Total Marks / 3

Example:

Total Marks = 229

Average Marks = 229 / 3

Average Marks = 76.33

# Pass or Fail Result

The result is determined by checking the marks of all three subjects.

If the student has marks greater than or equal to 40 in every subject:

Pass

Otherwise:

Fail

For example:

Subject 1 = 35
Subject 2 = 72
Subject 3 = 60

Since one subject has marks below 40, the result will be:

Fail

# How the StudentManager Works

The StudentManager manages multiple Student objects.

Conceptually:

StudentManager
       │
       ▼
List of Students
       │
       ├── Student 1
       ├── Student 2
       ├── Student 3
       ├── Student 4
       └── Student 5

When student records are loaded from a file:

1. The program reads each record.
2. A Student object is created.
3. The Student object is added to the StudentManager.
4. The StudentManager performs operations on the list.

# File Handling

File handling is used to store student records permanently.

Without file handling, all records would be lost when the program stops.

The project supports three file formats:

* TXT
* CSV
* JSON

# TXT File Handling

Student records can be stored in a TXT file.

Example:

101, Debmalya Ghosh, Computer Science, 5, 78, 82, 69
102, Priya Das, Computer Science, 5, 91, 87, 94

When loading the TXT file:

1. The file is opened in read mode.
2. Each line is read.
3. The line is cleaned using `strip()`.
4. The line is separated using `split(",")`.
5. Values are converted into appropriate data types.
6. A Student object is created.
7. The Student object is added to the student list.

When saving:

1. Each Student object is accessed.
2. The student information is converted into a comma-separated string.
3. The information is written to the TXT file.

# CSV File Handling

CSV files are handled using Python's built-in `csv` module.

Example CSV file:

Student_ID,Name,Department,Semester,Subject1,Subject2,Subject3
101,Debmalya Ghosh,Computer Science,5,78,82,69
102,Priya Das,Computer Science,5,91,87,94

When loading:

1. The CSV file is opened.
2. `csv.reader()` is used.
3. The header row is skipped.
4. Each row is read.
5. A Student object is created from each row.
6. The Student objects are returned.

When saving:

1. The CSV file is opened.
2. `csv.writer()` is used.
3. A header row is written.
4. Each Student object is written as a row.

# JSON File Handling

JSON files store data in a structured format.

Example:

{
    "student_id": 101,
    "name": "Debmalya Ghosh",
    "department": "Computer Science",
    "semester": 5,
    "marks": {
        "subject1": 78,
        "subject2": 82,
        "subject3": 69
    }
}

When loading:

1. The JSON file is opened.
2. `json.load()` reads the data.
3. The JSON data is converted into Python dictionaries and lists.
4. Student information is accessed.
5. A Student object is created.

Example values accessed:

item["student_id"]
item["name"]
item["department"]
item["semester"]
item["marks"]["subject1"]
item["marks"]["subject2"]
item["marks"]["subject3"]

When saving:

1. A dictionary is created for each Student object.
2. All student dictionaries are added to a list.
3. `json.dump()` writes the data into the JSON file.

# Command-Line Arguments

The project uses command-line arguments through the `argparse` module.

The user provides:

--file

and:

--format

The supported formats are:

txt
csv
json

Example:

  python3 main.py --file data/students.txt --format txt

The command tells the program:

* Which file should be loaded
* What type of file it is

# How to Run the Project

First, open the terminal inside the project folder.

Then use one of the following commands.

## Run Using TXT

  python3 main.py --file data/students.txt --format txt

## Run Using CSV

  python3 main.py --file data/students.csv --format csv

## Run Using JSON

  python3 main.py --file data/students.json --format json

On some systems, use:

  python main.py --file data/students.txt --format txt

instead of:

  python3 main.py --file data/students.txt --format txt

# Program Execution Flow

The overall execution flow is:

Command Line
      │
      ▼
main.py
      │
      ▼
Read Command-Line Arguments
      │
      ▼
Select File Format
      │
      ▼
file_handler.py
      │
      ▼
Load Student Records
      │
      ▼
Create Student Objects
      │
      ▼
StudentManager
      │
      ▼
Display Menu
      │
      ▼
User Selects an Operation
      │
      ├── Display
      ├── Add
      ├── Search
      ├── Update
      ├── Remove
      └── Save

# Program Menu

After starting the program, the following menu is displayed:

----- Student Record Management System -----

1. Display all students
2. Add new student
3. Search by Student ID
4. Search by Name
5. Search by Department
6. Search by Average Marks
7. Update student marks
8. Remove student
9. Save records
10. Exit

The user enters the corresponding number to perform an operation.

# Feature Explanation

## 1. Display All Students

The program displays all students currently available in the StudentManager.

For every student, the program displays:

* Student ID
* Name
* Department
* Semester
* Subject marks
* Total marks
* Average marks
* Result

## 2. Add New Student

The user enters:

Student ID
Name
Department
Semester
Subject 1 Marks
Subject 2 Marks
Subject 3 Marks

A new Student object is created.

The Student object is then added to the StudentManager.

A success message is displayed:

Student added successfully.

## 3. Search by Student ID

The user enters a Student ID.

The program checks every Student object.

Conceptually:

For every Student
        │
        ▼
Compare Student ID
        │
        ▼
    Is it equal?
   │            │
  Yes           No
   │             │
Display       Continue
Student         Loop

If no student is found:

Student not found.

## 4. Search by Name

The user enters a student name.

The program compares the entered name with the names stored in Student objects.

Matching student records are displayed.

If no matching student exists:

No student found.

## 5. Search by Department

The user enters a department name.

The program checks the department of every Student object.

All matching students are displayed.

For example:

  Computer Science

will display all students stored under the Computer Science department.

## 6. Search by Average Marks

The user enters a minimum average mark.

The program checks the average marks of every student.

Conceptually:

Student Average
       │
       ▼
Compare with Entered Value
       │
       ▼
Average Greater Than Condition?
       │
   Yes │ No
       │
       ▼
Display Student

Students satisfying the condition are displayed.

If no student satisfies the condition:

No student found.

## 7. Update Student Marks

The user enters the Student ID.

The program searches for the student.

If the student exists, the user enters new marks for:

* Subject 1
* Subject 2
* Subject 3

The `update_marks()` method updates the values.

The program displays:

Marks updated successfully.

## 8. Remove Student

The user enters a Student ID.

The program searches for the student.

If the student exists, the Student object is removed from the list.

The program displays:

Student removed successfully.

## 9. Save Records

The program saves the current list of students into the selected file.

The file format depends on the command-line argument.

Examples:

TXT  → save_to_txt()
CSV  → save_to_csv()
JSON → save_to_json()

After successful saving:

Records saved successfully.

## 10. Exit

The program stops when the user selects:

10

The message displayed is:

Exiting program.

# Searching Concepts Used

The searching operations are implemented using basic Python programming concepts.

The project does not use:

* Pandas
* NumPy
* External search libraries

Instead, the project uses:

* `for` loops
* `if` conditions
* Comparisons
* Lists

This makes the searching logic easy to understand.

# Input

The program accepts the following student information:

* Student ID
* Name
* Department
* Semester
* Subject 1 Marks
* Subject 2 Marks
* Subject 3 Marks

The program also accepts command-line arguments for:

* File path
* File format

# Output

The program displays student information in the terminal.

Example:

Student ID: 101
Name: Debmalya Ghosh
Department: Computer Science
Semester: 5
Subject 1 Marks: 78.0
Subject 2 Marks: 82.0
Subject 3 Marks: 69.0
Total Marks: 229.0
Average Marks: 76.33
Result: Pass

The program also displays messages for successful operations.

Examples:

Student added successfully.

Marks updated successfully.

Student removed successfully.

Records saved successfully.

For unsuccessful searches:

Student not found.

# Sample Student Records

The project was tested using multiple student records.

Example records include:

| Student ID | Name           | Department             | Semester |
| ---------- | -------------- | ---------------------- | -------- |
| 101        | Debmalya Ghosh | Computer Science       | 5        |
| 102        | Priya Das      | Computer Science       | 5        |
| 103        | Bazilur Rahman | Information Technology | 5        |
| 104        | Sneha Roy      | Electronics            | 5        |
| 105        | Sudip Dolui    | Computer Science       | 5        |

# Testing

The following features were tested successfully.

## Display All Students

All available student records were displayed successfully.

The output included:

* Student details
* Marks
* Total
* Average
* Result

## Search by Student ID

The program was tested using:

* An existing Student ID
* A non-existing Student ID

The correct student information was displayed for an existing ID.

For a non-existing ID:

Student not found.

was displayed correctly.

## Search by Name

The program was tested using:

* An existing student name
* A non-existing student name

The correct matching student was displayed.

For an invalid name:

No student found.

was displayed.

## Search by Department

The program successfully displayed students belonging to a selected department.

The program was also tested with a department that did not exist.

The correct message was displayed.

## Search by Average Marks

The program was tested using different minimum average marks.

Students satisfying the condition were displayed.

When no student matched:

No student found.

was displayed.

## Add Student

A new student was successfully added through the menu.

The program:

1. Accepted student information.
2. Created a Student object.
3. Added the Student object to the StudentManager.

## Update Student Marks

An existing student's marks were successfully updated.

The program:

1. Searched for the Student ID.
2. Found the student.
3. Accepted new marks.
4. Updated the Student object.

## Remove Student

A student was successfully removed.

The program:

1. Accepted the Student ID.
2. Searched for the student.
3. Removed the Student object from the list.

## Save Records

The current student records were saved successfully.

The save functionality was tested using the selected file format.

## TXT File Testing

The program was executed using:

  python3 main.py --file data/students.txt --format txt

The TXT records were successfully loaded.

The menu operations worked correctly.

Student records could also be saved.


## CSV File Testing

The program was executed using:

  python3 main.py --file data/students.csv --format csv

The CSV records were successfully loaded into Student objects.

The program operations worked correctly.

Updated records could be saved back into the CSV file.

## JSON File Testing

The program was executed using:

  python3 main.py --file data/students.json --format json

The JSON records were successfully loaded.

The nested marks data was processed correctly.

Student objects were created successfully.

Updated records could also be saved back into the JSON file.

# Recommended Screenshots

A `screenshots` folder can be created to store project screenshots.

Recommended structure:

screenshots/
├── project_structure.png
├── display_students.png
├── search_by_id.png
├── search_by_name.png
├── search_by_department.png
├── search_by_average.png
├── add_student.png
├── update_marks.png
├── remove_student.png
├── save_records.png
├── csv_execution.png
└── json_execution.png
```

Screenshots 



<img width="340" height="339" alt="image" src="https://github.com/user-attachments/assets/45523d53-dc99-457d-b948-17e5910a46da" />







# Learning Outcome

Through this project, I gained practical experience in developing a complete Python application using Object-Oriented Programming.

I learned how to:

* Create classes and objects
* Use constructors
* Work with attributes
* Create instance methods
* Manage multiple objects
* Organize a program into multiple Python files
* Use modular programming
* Read data from files
* Write data to files
* Work with TXT files
* Work with CSV files
* Work with JSON files
* Use command-line arguments
* Implement searching using loops and conditions
* Manage data using Python lists

The project also helped me understand how the same information can be stored and processed using different file formats.

# Challenges Faced

Some challenges faced during the development of this project included:

* Organizing the project into multiple Python files
* Connecting different modules together
* Managing multiple Student objects
* Loading records from different file formats
* Converting file data into Student objects
* Saving Student objects into TXT, CSV, and JSON files
* Implementing search operations using basic Python logic
* Maintaining consistent data across different file formats
* Testing the project using different command-line arguments

These challenges helped improve my practical understanding of Python programming.

# Conclusion

The Student Record Management and Search System was successfully developed using Python.

The project demonstrates the practical use of:

* Object-Oriented Programming
* Classes and Objects
* Modular Programming
* File Handling
* TXT Files
* CSV Files
* JSON Files
* Command-Line Arguments
* Searching
* Conditional Logic

The `Student` class represents individual student records, while the `StudentManager` class manages multiple Student objects.

The program successfully supports:

* Adding students
* Displaying students
* Searching students
* Updating marks
* Removing students
* Calculating total marks
* Calculating average marks
* Determining Pass or Fail results
* TXT file handling
* CSV file handling
* JSON file handling
* Command-line execution

The project was tested using multiple student records and all three supported file formats.

Overall, this project provided practical experience in building a structured Python application and improved my understanding of Object-Oriented Programming, file handling, modular programming, command-line arguments, and basic searching techniques.

# Author

**Debmalya Ghosh**

University of Calcutta
B.Tech in Computer Science and Engineering 
5th Semester
