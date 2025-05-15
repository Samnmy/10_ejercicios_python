members = {}
valid_plans = {"Basic", "Premium", "Elite"}

def register_member():
    member_id = input("Enter member ID: ").strip()
    if member_id in members:
        print("Error: Member ID already exists.")
        return
    name = input("Enter member name: ").strip()
    plan = input("Enter membership plan (Basic, Premium, Elite): ").strip()
    if plan not in valid_plans:
        print("Error: Invalid membership plan.")
        return
    members[member_id] = {
        "name": name,
        "plan": plan,
        "payment_status": True
    }
    print(f"Member '{name}' registered successfully.")

def update_membership_plan():
    member_id = input("Enter member ID to update: ").strip()
    if member_id not in members:
        print("Error: Member not found.")
        return
    new_plan = input("Enter new plan (Basic, Premium, Elite): ").strip()
    if new_plan not in valid_plans:
        print("Error: Invalid plan.")
        return
    members[member_id]["plan"] = new_plan
    print(f"Membership plan updated to '{new_plan}'.")

def mark_payment_status():
    member_id = input("Enter member ID: ").strip()
    if member_id not in members:
        print("Error: Member not found.")
        return
    status_input = input("Is payment up to date? (yes/no): ").strip().lower()
    if status_input not in {"yes", "no"}:
        print("Error: Please enter 'yes' or 'no'.")
        return
    members[member_id]["payment_status"] = (status_input == "yes")
    print("Payment status updated.")

def list_overdue_members():
    overdue = [info["name"] for info in members.values() if not info["payment_status"]]
    if not overdue:
        print("All members are up to date.")
    else:
        print("Members with overdue payments:")
        for name in overdue:
            print(f"- {name}")

def show_menu():
    print("\n--- Gym Membership System ---")
    print("1. Register new member")
    print("2. Update membership plan")
    print("3. Mark payment status")
    print("4. List overdue members")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            register_member()
        elif choice == "2":
            update_membership_plan()
        elif choice == "3":
            mark_payment_status()
        elif choice == "4":
            list_overdue_members()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
main()
