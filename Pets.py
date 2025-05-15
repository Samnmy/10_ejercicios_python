pets = []

def add_pet():
    name = input("Name: ")
    species = input("Species: ")
    try:
        age = int(input("Age: "))
        pets.append({"name": name, "species": species, "age": age})
        print("Pet added.\n")
    except ValueError:
        print("Invalid age.\n")

def search_by_species():
    species = input("Species to search: ")
    found = [p for p in pets if p["species"].lower() == species.lower()]
    for p in found:
        print(f'- {p["name"]} ({p["age"]} years)')
    print()

def filter_by_age():
    try:
        max_age = int(input("Maximum age: "))
        filtered = [p for p in pets if p["age"] <= max_age]
        for p in filtered:
            print(f'- {p["name"]} ({p["species"]}, {p["age"]} years)')
        print()
    except ValueError:
        print("Invalid age.\n")

def pet_menu():
    while True:
        print("----- Adoption Menu -----")
        print("1. Add pet")
        print("2. Search by species")
        print("3. Filter by age")
        print("4. Exit")
        option = input("Option: ")

        if option == "1": add_pet()
        elif option == "2": search_by_species()
        elif option == "3": filter_by_age()
        elif option == "4": break
        else: print("Invalid option.\n")

pet_menu()
