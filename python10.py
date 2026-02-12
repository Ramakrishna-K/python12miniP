from datetime import datetime

FILENAME = "expenses.txt"


# ---------- Amount Validation ----------
def get_valid_amount():
    while True:
        amount = input("Enter amount: ")
        try:
            return int(amount)
        except ValueError:
            print("❌ Please enter numbers only.")


# ---------- Add Expense ----------
def add_expense():
    amount = get_valid_amount()
    category = input("Enter category: ")

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, "a") as f:
        f.write(f"{amount}|{category}|{date_time}\n")

    print("✅ Expense saved!")


# ---------- View Expenses ----------
def view_expenses():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No expenses found")
            return

        print("\n--- Expenses ---")
        for i, line in enumerate(lines, start=1):
            parts = line.strip().split("|")

            # handles old data safely
            if len(parts) == 3:
                amount, category, date_time = parts
            else:
                amount, category = parts
                date_time = "N/A"

            print(f"{i}. ₹{amount} - {category} - {date_time}")

    except FileNotFoundError:
        print("No file found")


# ---------- Delete Expense ----------
def delete_expense():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No expenses to delete")
            return

        view_expenses()
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(lines):
            lines.pop(choice - 1)

            with open(FILENAME, "w") as f:
                f.writelines(lines)

            print("🗑️ Expense deleted successfully!")
        else:
            print("❌ Invalid number")

    except FileNotFoundError:
        print("No file found")
    except ValueError:
        print("❌ Enter a valid number")


# ---------- Category Total ----------
def category_total():
    totals = {}

    try:
        with open(FILENAME, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                amount = int(parts[0])
                category = parts[1]

                totals[category] = totals.get(category, 0) + amount

        print("\n--- Category Totals ---")
        for cat, amt in totals.items():
            print(f"{cat}: ₹{amt}")

    except FileNotFoundError:
        print("No data available")


# ---------- Menu ----------
def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Category Total")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            category_total()
        elif choice == "5":
            print("👋 Good bye RK")
            break
        else:
            print("❌ Invalid choice")


menu()
