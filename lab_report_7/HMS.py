from abc import ABC, abstractmethod


class staff(ABC):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    @abstractmethod
    def get_details(self):
        pass


class doctor(staff):
    def __init__(self, name, age, department, specialization, patients_assigned=None):
        super().__init__(name, age, department)
        self.specialization = specialization
        self.patients_assigned = patients_assigned if patients_assigned is not None else []

    def get_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"specialization: {self.specialization}")
        if self.patients_assigned:
            print("patients assigned:")
            for patient in self.patients_assigned:
                print(patient)
        else:
            print("no patients assigned.")


class nurse(staff):
    def __init__(self, name, age, department, shift, wards_assigned=None):
        super().__init__(name, age, department)
        self.shift = shift
        self.wards_assigned = wards_assigned if wards_assigned is not None else []

    def get_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"shift: {self.shift}")
        if self.wards_assigned:
            print("wards assigned:")
            for ward in self.wards_assigned:
                print(ward)
        else:
            print("no wards assigned.")


class administrative_staff(staff):
    def __init__(self, name, age, department, designation=None):
        super().__init__(name, age, department)
        self.designation = designation if designation is not None else ""

    def get_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"designation: {self.designation}")


doctor = doctor("bishwajit", 22, "medicine", "cardiology")
doctor.get_details()

print("\n")

nurse = nurse("urmi", 23, "nursing", "day shift", ["ward a", "ward b"])
nurse.get_details()

print("\n")

administrative_staff = administrative_staff("shah alom", 25, "hr", "manager")
administrative_staff.get_details()