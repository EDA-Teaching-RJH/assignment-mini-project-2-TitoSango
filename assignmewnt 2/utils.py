import csv
import re
import statistics
from student import Student


# Validate names using regex
# Allows letters, spaces and hyphens only
def is_valid_name(name):
    pattern = r'^[A-Za-z]+(?:[ -][A-Za-z]+)*$'
    return re.fullmatch(pattern, name) is not None


# Validate emails using regex
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email) is not None


# Validate marks before converting to integer
def is_valid_mark(mark_text):
    pattern = r'^\d+$'
    return re.fullmatch(pattern, mark_text) is not None


# Read students from CSV file and keep only valid rows
def read_students(filename):
    students = []

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) != 3:
                print(f"Invalid row skipped: {row}")
                continue

            name = row[0].strip()
            email = row[1].strip()
            mark_text = row[2].strip()

            if not is_valid_name(name):
                print(f"Invalid name skipped: {name}")
                continue

            if not is_valid_email(email):
                print(f"Invalid email skipped: {email}")
                continue

            if not is_valid_mark(mark_text):
                print(f"Invalid mark skipped: {mark_text}")
                continue

            mark = int(mark_text)
            students.append(Student(name, email, mark))

    return students


# Calculate average mark of valid students
def calculate_average(students):
    if len(students) == 0:
        return 0
    marks = [student.mark for student in students]
    return statistics.mean(marks)


# Write processed student report to a text file
def write_report(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(
                f"{student.name} - {student.email} - {student.mark} - {student.get_grade()}\n"
            )


# Count how many students got each grade
def grade_summary(students):
    summary = {"A": 0, "B": 0, "C": 0, "F": 0}

    for student in students:
        grade = student.get_grade()
        summary[grade] += 1

    return summary


# Find the highest scoring student
def find_top_student(students):
    if len(students) == 0:
        return None
    return max(students, key=lambda student: student.mark)