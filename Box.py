warehouse = {}

def add_box_type():
    box_type = input("Box type: ")
    try:
        quantity = int(input("Initial quantity: "))
        warehouse[box_type] = quantity
        print("Box type added.\n")
    except ValueError:
        print("Invalid quantity.\n")

def update_quantity():
    box_type = input("Box type: ")
    if box_type in warehouse:
        try:
            quantity = int(input("New quantity: "))
            warehouse[box_type] = quantity
            print("Quantity updated.\n")
        except ValueError:
            print("Invalid quantity.\n")
    else:
        print("Box type not found.\n")

def check_availability():
    box_type = input("Box type to check: ")
    try:
        required_quantity = int(input("Required quantity: "))
        if warehouse.get(box_type, 0) >= required_quantity:
            print("Sufficient quantity available.\n")
        else:
            print("Insufficient quantity.\n")
    except ValueError:
        print("Invalid quantity.\n")

def warehouse_menu():
    while True:
        print("----- Warehouse Menu -----")
        print("1. Add box type")
        print("2. Update quantity")
        print("3. Check sufficient quantity")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            add_box_type()
        elif option == "2":
            update_quantity()
        elif option == "3":
            check_availability()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

warehouse_menu()
