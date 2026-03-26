from student import Student
from utils import is_valid_email, calculate_average


def test_grade():
    s = Student("Test", "test@test.com", 75)
    assert s.get_grade() == "A"

    s2 = Student("Test", "test@test.com", 65)
    assert s2.get_grade() == "B"

    s3 = Student("Test", "test@test.com", 50)
    assert s3.get_grade() == "C"

    s4 = Student("Test", "test@test.com", 40)
    assert s4.get_grade() == "F"


def test_email():
    assert is_valid_email("valid@email.com")
    assert not is_valid_email("invalidemail.com")


def test_average():
    students = [
        Student("A", "a@test.com", 80),
        Student("B", "b@test.com", 60)
    ]
    assert calculate_average(students) == 70