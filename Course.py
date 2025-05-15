courses = []

def register_course():
    title = input("Title: ")
    try:
        duration = int(input("Duration (hours): "))
        enrolled = int(input("Enrolled: "))
        courses.append({"title": title, "duration": duration, "enrolled": enrolled})
        print("Course registered.\n")
    except ValueError:
        print("Invalid data.\n")

def update_enrollment():
    title = input("Course title: ")
    for c in courses:
        if c["title"].lower() == title.lower():
            try:
                new_enrollment = int(input("New number of enrolled: "))
                c["enrolled"] = new_enrollment
                print("Enrollment updated.\n")
                return
            except ValueError:
                print("Invalid quantity.\n")
    print("Course not found.\n")

def filter_by_duration():
    try:
        min_duration = int(input("Minimum duration (hours): "))
        filtered = [c for c in courses if c["duration"] >= min_duration]
        print("Filtered courses:")
        for c in filtered:
            print(f'- {c["title"]} ({c["duration"]}h)')
        print()
    except ValueError:
        print("Invalid duration.\n")

def course_menu():
    while True:
        print("----- Course Menu -----")
        print("1. Register course")
        print("2. Update enrollment")
        print("3. Filter by duration")
        print("4. Exit")
        option = input("Option: ")

        if option == "1":
            register_course()
        elif option == "2":
            update_enrollment()
        elif option == "3":
            filter_by_duration()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

course_menu()
