students = {}  

def display_student_data():
    if len(students)==0:  
        print("No Students")  
        return 

    for student in students.values(): 
        print(f"Name: {student['name']}")
        print(f"Roll No: {student['roll_no']}") 
        print(f"Age: {student['age']:.2f}")

while True:  
    print("\nChoose an option:") 
    print("1. Add Student") 
    print("2. Display Student Data") 
    print("3. Exit")   

    choice = input("Enter your choice (1/2/3): ")
    name_input=""
    roll_no_input=0
    age_input=0.00

    if choice == '1':
        checker = int(input("enter 1 for enter name: "))
        if checker==1:
            name_input = input("Enter student's name: (max 5 characters): ")
        else:
            print("Invalid choice")
        checker = int(input("enter 1 for enter roll: "))
        if checker==1:
            roll_no_input = int(input("Enter student's Roll No: "))
        else:
            print("Invalid choice")
        checker = int(input("enter 1 for enter age: "))
        if checker==1:
            age_input = float(input("Enter student's age (float): "))
        else:
            print("Invalid choice")

        students[roll_no_input] = { "name": name_input, "roll_no": roll_no_input, "age": age_input } 
        print("Student added.")  
    elif choice == '2': 
        display_student_data()  
    elif choice == '3':  
        print("Exiting")
        break 
    else:
        print("Invalid choice")

