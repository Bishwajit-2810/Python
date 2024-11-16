class Student:
    def __init__(self, name, student_id, email, major):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.major = major

    def get_details(self):
        details = f"Name: {self.name}\nStudent ID: {self.student_id}\nEmail: {self.email}\nMajor: {self.major}"
        return details


class RegularStudent(Student):
    def __init__(self, name, student_id, email, major):
        super().__init__(name, student_id, email, major)

    def get_details1(self):
        return self.get_details()


class ExchangeStudent(Student):
    def __init__(self, name, student_id, email, major, home_university):
        super().__init__(name, student_id, email, major)
        self.home_university = home_university

    def get_details1(self):
        details = f"{super().get_details()}\nHome University: {self.home_university}"
        return details


def print_student_details(students):
    for student in students:
        print(student.get_details())
        print("-" * 30)


# Example usage:

regular_student = RegularStudent("Bishwajit", "1414", "bishwajit@gmail.com", "Computer Science")
exchange_student = ExchangeStudent("Shah Alom", "1409", "shahalam@gmail.com", "Mechanical Engineering", "University of California, Berkeley")

students = [regular_student, exchange_student]
print_student_details(students)