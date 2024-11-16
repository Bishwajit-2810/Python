from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email

    @abstractmethod
    def get_info(self):
        pass


class Undergraduate(Student):
    def __init__(self, name, student_id, email, year):
        super().__init__(name, student_id, email)
        self.year = year

    def get_info(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\nEmail: {self.email}\nYear: {self.year}"


class Graduate(Student):
    def __init__(self, name, student_id, email, research_topic):
        super().__init__(name, student_id, email)
        self.research_topic = research_topic

    def get_info(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\nEmail: {self.email}\nResearch Topic: {self.research_topic}"


def print_student_info(students):
    for student in students:
        if isinstance(student, Undergraduate):
            print(f"Undergraduate Student\n{student.get_info()}")
        elif isinstance(student, Graduate):
            print(f"Graduate Student\n{student.get_info()}")


# Example usage:

undergraduate = Undergraduate("Bishwajit", "1414", "bishwajit@gmail.com","2026")
print(undergraduate.get_info())

graduate = Graduate("Shah Alom", "1409", "shahalam@gmail.com", "Machine Learning for Natural Language Processing")
print(graduate.get_info())

students = [undergraduate, graduate]
print_student_info(students)