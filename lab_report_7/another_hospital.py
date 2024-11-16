class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Gender: {self.gender}")


class Patient(Person):
    def __init__(self, patient_id, name, age, gender, diagnosis, email=""):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.email = email

    def display_details(self):
        super().display_details()
        print(f"Patient ID: {self.patient_id}")
        print(f"Diagnosis: {self.diagnosis}")
        if self.email:
            print(f"Email: {self.email}")


class InPatient(Patient):
    def __init__(self, patient_id, name, age, gender, diagnosis, room_number, admission_date, email=""):
        super().__init__(patient_id, name, age, gender, diagnosis, email)
        self.room_number = room_number
        self.admission_date = admission_date

    def display_details(self):
        super().display_details()
        print(f"Room Number: {self.room_number}")
        print(f"Admission Date: {self.admission_date}")


patient1 = Patient("P001", "Bishwajit", 22, "Male", "cold")
in_patient1 = InPatient("I001", "Shah Alom", 25, "Female", "Diabetes", "Room 101", "2022-01-01")

print("\nPatient Details:")
patient1.display_details()
print("\nIn Patient Details:")
in_patient1.display_details()
