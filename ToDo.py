tasks = []

def add_task():
    desc = input("Description: ")
    priority = input("Priority (high/medium/low): ").lower()
    tasks.append({"desc": desc, "priority": priority, "completed": False})
    print("Task added.\n")

def mark_completed():
    desc = input("Task description to mark: ")
    for t in tasks:
        if t["desc"].lower() == desc.lower():
            t["completed"] = True
            print("Task marked as completed.\n")
            return
    print("Task not found.\n")

def filter_tasks():
    criterion = input("Filter by (priority/completed): ").lower()
    if criterion == "priority":
        value = input("Priority to filter: ").lower()
        filtered = [t for t in tasks if t["priority"] == value]
    elif criterion == "completed":
        value = input("Show only completed? (y/n): ").lower() == "y"
        filtered = [t for t in tasks if t["completed"] == value]
    else:
        print("Invalid criterion.\n")
        return

    for t in filtered:
        status = "Completed" if t["completed"] else "Pending"
        print(f'- {t["desc"]} ({t["priority"]}, {status})')
    print()

def task_menu():
    while True:
        print("----- Task Menu -----")
        print("1. Add task")
        print("2. Mark as completed")
        print("3. Filter tasks")
        print("4. Exit")
        option = input("Option: ")

        if option == "1": add_task()
        elif option == "2": mark_completed()
        elif option == "3": filter_tasks()
        elif option == "4": break
        else: print("Invalid option.\n")

task_menu()
