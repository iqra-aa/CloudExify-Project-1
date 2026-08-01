# CloudExify-Project-1

# Personal Expense Tracker

A command-line based Personal Expense Tracker built using Python.

This project was developed as part of the CloudExify Python Internship 2026 - Month 1 Project.

---

## Project Description

The Personal Expense Tracker is a CLI application that allows users to manage their daily expenses.

Users can:
- Add expenses
- View all expenses
- Calculate total spending
- View spending by category
- Search expenses by category
- Edit expenses
- Delete expenses
- Save and load expense data using CSV files

---

## Features

### Expense Management
- Add new expenses with:
  - Amount
  - Category
  - Description

- View expenses in a formatted table

- Edit existing expenses

- Delete expenses by ID


### Reports

- Total expense calculation

- Category-wise spending summary

- Search expenses by category


### Data Storage

- Expenses are saved permanently in a CSV file.

- Previous expenses automatically load when the application starts.

---

## Technologies Used

- Python 3.x
- CSV File Handling
- Object-Oriented Programming Concepts
- Command Line Interface (CLI)

---

## Project Structure

```

ExpenseTracker/

│
├── main.py
│       Main program and menu system
│
├── expense_manager.py
│       Expense management functions
│
├── file_handler.py
│       CSV save and load operations
│
├── utils.py
│       Helper functions and input validation
│
├── expenses.csv
│       Stored expense data
│
└── README.md
Project documentation

```

---

## How to Run

### 1. Clone the repository

```

git clone your-repository-link

```

### 2. Open the project folder

```

cd ExpenseTracker

```

### 3. Run the application

```

python main.py

```

---

## Example Usage

```

==============================
PERSONAL EXPENSE TRACKER
========================

1. Add Expense
2. View All Expenses
3. View Total Expenses
4. View Category Summary
5. Search Expense by Category
6. Edit Expense
7. Delete Expense
8. Save Expenses
9. Exit

```

---

## Learning Outcomes

Through this project, the following Python concepts were practiced:

- Variables and data types
- Functions
- Lists and dictionaries
- Loops and conditions
- File handling
- CSV data storage
- Exception handling
- Code organization

---

## Future Improvements

Possible improvements:

- Add expense dates
- Add monthly reports
- Add graphical interface
- Add database support
- Add user authentication

---





