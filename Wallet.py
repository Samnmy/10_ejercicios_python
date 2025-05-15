expenses = {}

def register_expense():
    category = input("Category: ")
    try:
        amount = float(input("Amount: "))
        expenses[category] = expenses.get(category, 0) + amount
        print("Expense recorded.\n")
    except ValueError:
        print("Invalid amount.\n")

def total_spent():
    total = sum(expenses.values())
    print(f"Total spent: ${total:.2f}\n")

def percentage_by_category():
    total = sum(expenses.values())
    if total == 0:
        print("No expenses recorded.\n")
        return
    for cat, amount in expenses.items():
        percent = (amount / total) * 100
        print(f"{cat}: {percent:.2f}%")
    print()

def wallet_menu():
    while True:
        print("----- Wallet Menu -----")
        print("1. Register expense")
        print("2. Calculate total spent")
        print("3. Percentage by category")
        print("4. Exit")
        option = input("Option: ")

        if option == "1": register_expense()
        elif option == "2": total_spent()
        elif option == "3": percentage_by_category()
        elif option == "4": break
        else: print("Invalid option.\n")

wallet_menu()
