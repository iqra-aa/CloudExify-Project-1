from collections import defaultdict


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, amount, category, description):
        expense = {
            "id": self.next_id,
            "amount": amount,
            "category": category.title(),
            "description": description
        }

        self.expenses.append(expense)
        self.next_id += 1

        print("\n✅ Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.")
            return

        print("\n" + "=" * 75)
        print(f"{'ID':<5}{'Amount':<12}{'Category':<20}{'Description'}")
        print("=" * 75)

        for expense in self.expenses:
            print(
                f"{expense['id']:<5}"
                f"{expense['amount']:<12.2f}"
                f"{expense['category']:<20}"
                f"{expense['description']}"
            )

        print("=" * 75)

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)

        print("\n========== TOTAL EXPENSES ==========")
        print(f"Total Spending : ${total:.2f}")

    def category_summary(self):
        if not self.expenses:
            print("\nNo expenses available.")
            return

        summary = defaultdict(float)

        for expense in self.expenses:
            summary[expense["category"]] += expense["amount"]

        print("\n====== EXPENSES BY CATEGORY ======")

        for category, total in summary.items():
            print(f"{category:<20} ${total:.2f}")

    def search_category(self, category):
        found = False

        print("\nSearch Results\n")

        for expense in self.expenses:
            if expense["category"].lower() == category.lower():
                print(
                    f"ID: {expense['id']} | "
                    f"Amount: ${expense['amount']:.2f} | "
                    f"{expense['description']}"
                )
                found = True

        if not found:
            print("No expenses found in this category.")

    def edit_expense(self, expense_id):
        for expense in self.expenses:
            if expense["id"] == expense_id:

                print("\nLeave blank to keep current value.\n")

                amount = input(f"Amount ({expense['amount']}): ")
                category = input(f"Category ({expense['category']}): ")
                description = input(
                    f"Description ({expense['description']}): "
                )

                if amount:
                    try:
                        expense["amount"] = float(amount)
                    except ValueError:
                        print("Invalid amount. Old value kept.")

                if category:
                    expense["category"] = category.title()

                if description:
                    expense["description"] = description

                print("\n✅ Expense updated successfully!")
                return

        print("Expense ID not found.")

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                print("\n✅ Expense deleted successfully!")
                return

        print("Expense ID not found.")

    def get_expenses(self):
        return self.expenses

    def load_expenses(self, expenses):
        self.expenses = expenses

        if expenses:
            self.next_id = max(expense["id"] for expense in expenses) + 1
        else:
            self.next_id = 1