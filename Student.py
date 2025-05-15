students = {}

def add_student():
    name = input("Student name: ")
    if name not in students:
        students[name] = []
        print(f'Student "{name}" added.\n')
    else:
        print("Student already exists.\n")

def register_grade():
    name = input("Student name: ")
    if name in students:
        try:
            grade = float(input("Enter grade: "))
            students[name].append(grade)
            print("Grade recorded.\n")
        except ValueError:
            print("Invalid grade.\n")
    else:
        print("Student not found.\n")

def calculate_average():
    name = input("Student name: ")
    if name in students and students[name]:
        average = sum(students[name]) / len(students[name])
        print(f"Average for {name}: {average:.2f}\n")
    else:
        print("No grades recorded for this student.\n")

def grade_menu():
    while True:
        print("----- Grade Menu -----")
        print("1. Add student")
        print("2. Register grade")
        print("3. Calculate average")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1": add_student()
        elif option == "2": register_grade()
        elif option == "3": calculate_average()
        elif option == "4": break
        else: print("Invalid option.\n")

grade_menu()
