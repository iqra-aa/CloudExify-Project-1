from expense_manager import ExpenseManager
from file_handler import save_expenses, load_expenses
from utils import (
    print_header,
    get_float,
    get_non_empty_input,
    get_int,
    confirm_action
)


def show_menu():
    print("""
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. View Category Summary
5. Search Expense by Category
6. Edit Expense
7. Delete Expense
8. Save Expenses
9. Exit
""")


def main():

    manager = ExpenseManager()

    # Load previous expenses
    old_expenses = load_expenses()
    manager.load_expenses(old_expenses)

    print_header("PERSONAL EXPENSE TRACKER")

    if old_expenses:
        print(f"Loaded {len(old_expenses)} previous expenses.")

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        # Add expense
        if choice == "1":

            print_header("ADD EXPENSE")

            amount = get_float("Enter amount: ")
            category = get_non_empty_input("Enter category: ")
            description = get_non_empty_input("Enter description: ")

            manager.add_expense(
                amount,
                category,
                description
            )


        # View expenses
        elif choice == "2":

            print_header("ALL EXPENSES")

            manager.view_expenses()


        # Total expenses
        elif choice == "3":

            print_header("TOTAL EXPENSES")

            manager.total_expenses()


        # Category summary
        elif choice == "4":

            print_header("CATEGORY SUMMARY")

            manager.category_summary()


        # Search category
        elif choice == "5":

            print_header("SEARCH CATEGORY")

            category = get_non_empty_input(
                "Enter category: "
            )

            manager.search_category(category)


        # Edit expense
        elif choice == "6":

            print_header("EDIT EXPENSE")

            expense_id = get_int(
                "Enter expense ID: "
            )

            manager.edit_expense(expense_id)


        # Delete expense
        elif choice == "7":

            print_header("DELETE EXPENSE")

            expense_id = get_int(
                "Enter expense ID: "
            )

            if confirm_action(
                "Are you sure you want to delete?"
            ):
                manager.delete_expense(expense_id)

            else:
                print("Deletion cancelled.")


        # Save expenses
        elif choice == "8":

            save_expenses(
                manager.get_expenses()
            )


        # Exit
        elif choice == "9":

            print("\nSaving data before exit...")

            save_expenses(
                manager.get_expenses()
            )

            print("Thank you for using Expense Tracker!")
            break


        else:
            print("\n❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()