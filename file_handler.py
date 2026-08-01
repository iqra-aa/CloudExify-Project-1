import csv
import os


FILE_NAME = "expenses.csv"


def save_expenses(expenses):
    """
    Save all expenses to a CSV file.
    """

    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Header row
            writer.writerow([
                "ID",
                "Amount",
                "Category",
                "Description"
            ])

            # Expense rows
            for expense in expenses:
                writer.writerow([
                    expense["id"],
                    expense["amount"],
                    expense["category"],
                    expense["description"]
                ])

        print("\n✅ Expenses saved successfully!")

    except Exception as error:
        print(f"\nError while saving file: {error}")


def load_expenses():
    """
    Load expenses from the CSV file.
    Returns a list of expense dictionaries.
    """

    expenses = []

    # If file doesn't exist yet
    if not os.path.exists(FILE_NAME):
        return expenses

    try:

        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                expense = {
                    "id": int(row["ID"]),
                    "amount": float(row["Amount"]),
                    "category": row["Category"],
                    "description": row["Description"]
                }

                expenses.append(expense)

    except Exception as error:
        print(f"\nError while loading file: {error}")

    return expenses