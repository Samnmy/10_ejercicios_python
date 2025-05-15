menu = []

def add_dish():
    name = input("Dish name: ")
    try:
        price = float(input("Dish price: "))
        available = input("Is it available? (y/n): ").lower() == 'y'
        menu.append({"name": name, "price": price, "available": available})
        print("Dish added.\n")
    except ValueError:
        print("Invalid price.\n")

def toggle_availability():
    name = input("Dish name to modify: ")
    for dish in menu:
        if dish["name"].lower() == name.lower():
            dish["available"] = not dish["available"]
            status = "available" if dish["available"] else "not available"
            print(f"Availability updated to {status}.\n")
            return
    print("Dish not found.\n")

def count_available_dishes():
    count = sum(1 for dish in menu if dish["available"])
    print(f"Total available dishes: {count}\n")

def restaurant_menu():
    while True:
        print("----- Restaurant Menu -----")
        print("1. Add dish")
        print("2. Modify availability")
        print("3. Count available dishes")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1": add_dish()
        elif option == "2": toggle_availability()
        elif option == "3": count_available_dishes()
        elif option == "4": break
        else: print("Invalid option.\n")

restaurant_menu()
