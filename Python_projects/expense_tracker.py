'''
Personal Expense Tracker
Description: Build a program to track personal expenses. It should allow users to add, delete, and view expenses. Summarize expenses by category (e.g., food, transport).
Key Concepts: File handling, data structures (dictionaries/lists), input validation.


'''

class Personal_expense_tracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = {}

    def Add_expense(self):
        category = input("Enter the Category of your expense\ne.g Food , Transportation\n").strip().lower()
        amount = int(input("Enter the amount:- "))

        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

        self.budget -= amount
        print(f'Expense of {amount} added to the {category}\nRemaining budget {self.budget}')

    def view_expenses(self):
        print("Expenses Summery")
        if not self.expenses:
            print("No Expenses Recorded yet")
        else:
            for category, amount in self.expenses.items():
                print(f'Category {category.capitalize()}: {amount}')   
        print(f'Remaining Budget : {self.budget}\n')


shivam = Personal_expense_tracker(80000)
# shivam.Add_expense()
shivam.view_expenses()