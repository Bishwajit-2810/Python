class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.admission_date = None
        self.room_number = None
        self.appointment_time = None

    def get_patient_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.admission_date:
            print(f"Admission Date: {self.admission_date}")
        if self.room_number:
            print(f"Room Number: {self.room_number}")
        if self.appointment_time:
            print(f"Appointment Time: {self.appointment_time}")


class InPatient(Patient):
    def __init__(self, name, age, admission_date, room_number):
        super().__init__(name, age)
        self.admission_date = admission_date
        self.room_number = room_number

    def get_patient_info(self):
        super().get_patient_info()
        print(f"Room Number: {self.room_number}")


class OutPatient(Patient):
    def __init__(self, name, age, appointment_time):
        super().__init__(name, age)
        self.appointment_time = appointment_time

    def get_patient_info(self):
        super().get_patient_info()
        print(f"Appointment Time: {self.appointment_time}")


inpatient1 = InPatient("Bishwajit", 22, "2022-01-01", "Room 101")
outpatient1 = OutPatient("Urmi", 23, "12:00 AM")

inpatient2 = InPatient("Shah alom", 25, "2022-02-15", "Room 202")
outpatient2 = OutPatient("Likhon", 20, "06:00 PM")

inpatient1.get_patient_info()
print("\n")
outpatient1.get_patient_info()

print("\n")

inpatient2.get_patient_info()
print("\n")
outpatient2.get_patient_info()