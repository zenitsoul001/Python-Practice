class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = {
            "Name" : name,
            "Amount" : amount,
            "Category" : category
        }
        self.expenses.append(expense)
        return self.expenses

    def view_expenses(self):
        if not self.expenses:
            print("No Expenses Added Yet")
        
        for expense in self.expenses:
            print(f"\nName : {expense['Name']} | Amount : {expense['Amount']} | Category : {expense['Category']}")

    def total_spending(self):
        total = 0
        for expense in self.expenses:
            total += expense["Amount"]
        return total

    def exit_exp(self):
        print("Thank you for using the Expense Tracker. Goodbye!")

    ## Expense Tracker
    def run(self):
        while(True):
            print("""\n********* EXPENSE TRACKER ********
            1. Add Expense
            2. View All Expenses
            3. View Total Spendings
            4. Exit""")

            try:
                user_inp = int(input("Enter your choice (1-4): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            if user_inp == 1:
                name = input("Enter the Name of your Expense: ")
                while True:
                    try:
                        amount = float(input("Enter the Amount of your Expense: "))
                        break
                    except ValueError:
                        print("Invalid input for amount. Please enter a valid number.")
                    except TypeError:
                        print("Invalid input for amount. Please enter a valid number.")
                    continue
                category = input("Enter the Category of your Expense: ")
                self.add_expense(name, amount, category)
                print("Expense Added Successfully!")

            elif user_inp == 2:
                self.view_expenses()

            elif user_inp == 3:
                print(f"Total Spending: {self.total_spending()}")

            elif user_inp == 4:
                self.exit_exp()
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.") 

ET = ExpenseTracker()
ET.run()