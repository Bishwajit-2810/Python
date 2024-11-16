class doctor:
    def __init__(self, name):
        self.name = name

    def diagnose(self, patient):
        print(f"{self.name} is diagnosing the patient.")

    def prescribe_medicine(self, patient, medicine):
        print(f"{self.name} has prescribed {medicine} to the patient.")


class cardiologist(doctor):
    def __init__(self, name, years_of_experience):
        super().__init__(name)
        self.years_of_experience = years_of_experience

    def perform_ecg(self, patient):
        print(f"{self.name} is performing ECG on {patient.name}.")
        import time
        time.sleep(2)
        print(f"ECG done. Results will be analyzed.")

    def analyze_ecg_results(self, patient, results):
        print(f"{self.name} is analyzing the ECG results for {patient.name}.")
        import time
        time.sleep(1)
        print(f"ECG results: {results}")


class neurologist(doctor):
    def __init__(self, name, specialization_area):
        super().__init__(name)
        self.specialization_area = specialization_area

    def perform_neurological_exam(self, patient):
        print(f"{self.name} is performing the neurological exam for {patient.name}.")
        import time
        time.sleep(1)
        print("Neurological exam done.")

    def diagnose_neurological_condition(self, patient, condition):
        print(f"{self.name} is diagnosing the {condition} in {patient.name}.")
        import time
        time.sleep(2)
        print(f"Diagnosis confirmed: {condition}")


class Patient:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_patient_info(self):
        return f"Name: {self.name}, Email: {self.email}"


doctor = doctor("bishwajit@gmail.com")
cardiologist = cardiologist("shah alom@yahoo.com", 10)

patient1 = Patient("John Doe", "john.doe@example.com")
print(patient1.get_patient_info())

doctor.diagnose(patient1)
cardiologist.prescribe_medicine(patient1, "aspirin")

cardiologist.perform_ecg(patient1)
cardiologist.analyze_ecg_results(patient1, "normal ecg results")

neurologist = neurologist("shah alom@hotmail.com", "neurology")

patient2 = Patient("Shafi", "jane.doe@gmail.com")
print(patient2.get_patient_info())

neurologist.diagnose_neurological_condition(patient2, "migraine")