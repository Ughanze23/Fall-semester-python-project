# Fall-semester-python-project


Expense Tracker: A simple Python library for managing your finances
This README file describes Expense Tracker, a Python library that provides simple classes and methods for managing your personal expenses.This README also explains how to clone  and run the code on your own PC, and highlights the key features of your classes

Project Features:
* 2 classes , class 1 : Expense has 3 methods, class 2 (ExpenseDatabase) has 6 methods
### Expense Class:
* Create expense objects with title, amount, and timestamps.
* Update existing expenses by changing title or amount.
* return expense as a dictionary
### ExpenseDatabase Class :  
* Store expenses in a database-like structure.
* Retrieve expenses by ID or title.
* Delete expense from database
* Export all expenses as a list of dictionaries.

# how to run it
Clone the repository using git clone https://github.com/Ughanze23/Fall-semester-python-project.git

# Running the Code:

The provided code sample in the README demonstrates how to use the classes and methods. You can copy and paste the code into your own Python environment to test and explore the functionality.

Classes:
Expense: Represents an individual expense with title, amount, ID, creation and update timestamps.
ExpenseDatabase: Represents a collection of Expenses, offering methods to add, remove, retrieve, and export expenses.
Example Usage:
```
# Create some expenses
expense1 = Expense("Groceries", 4500)
expense2 = Expense("Fuel", 20000)

# Add them to the database
db = ExpenseDatabase()
db.add_expense(expense1)
db.add_expense(expense2)

# Update an expense
expense1.update(title="Food")

# Retrieve an expense by ID
retrieved_expense = db.get_expense_by_id(expense1.id)

# Get all expenses as a list of dictionaries
expense_dicts = db.to_dict()

# ... and so on ```
