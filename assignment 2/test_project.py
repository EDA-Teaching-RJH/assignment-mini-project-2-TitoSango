from student import Student
from utils import (
    is_valid_name,
    is_valid_email,
    is_valid_mark,
    calculate_average,
    grade_summary,
    find_top_student
)


def test_get_grade_a():
    student = Student("Alice Smith", "alice@gmail.com", 78)
    assert student.get_grade() == "A"


def test_get_grade_b():
    student = Student("Bob Jones", "bob@gmail.com", 64)
    assert student.get_grade() == "B"


def test_get_grade_c():
    student = Student("Charlie Brown", "charlie@gmail.com", 55)
    assert student.get_grade() == "C"


def test_get_grade_f():
    student = Student("Eve White", "eve@gmail.com", 40)
    assert student.get_grade() == "F"


def test_valid_name():
    assert is_valid_name("Alice Smith")


def test_invalid_name():
    assert not is_valid_name("Alice123")


def test_valid_email():
    assert is_valid_email("alice.smith@gmail.com")


def test_invalid_email():
    assert not is_valid_email("alice.smithgmail.com")


def test_valid_mark():
    assert is_valid_mark("78")


def test_invalid_mark():
    assert not is_valid_mark("7A")


def test_calculate_average():
    students = [
        Student("A One", "a@test.com", 80),
        Student("B Two", "b@test.com", 60)
    ]
    assert calculate_average(students) == 70


def test_grade_summary():
    students = [
        Student("A One", "a@test.com", 80),
        Student("B Two", "b@test.com", 65),
        Student("C Three", "c@test.com", 55),
        Student("D Four", "d@test.com", 40)
    ]
    summary = grade_summary(students)
    assert summary == {"A": 1, "B": 1, "C": 1, "F": 1}


def test_find_top_student():
    students = [
        Student("A One", "a@test.com", 80),
        Student("B Two", "b@test.com", 92),
        Student("C Three", "c@test.com", 55)
    ]
    top_student = find_top_student(students)
    assert top_student.name == "B Two"
    assert top_student.mark == 92