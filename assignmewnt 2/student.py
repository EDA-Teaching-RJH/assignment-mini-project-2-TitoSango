# Parent class representing a person
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, email, mark):
        super().__init__(name, email)
        self.mark = mark

    # Calculate grade based on mark
    def get_grade(self):
        if self.mark >= 70:
            return "A"
        elif self.mark >= 60:
            return "B"
        elif self.mark >= 50:
            return "C"
        else:
            return "F"
        
        # Class representing a student and their grade logic