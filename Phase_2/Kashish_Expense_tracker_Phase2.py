class ExpenseTracker:
    expenses = []
    expense = {}
    def add_expense(self, name, amount, category):
        self.expense = {
            "Name" : name,
            "Amount" : amount,
            "Category" : category
        }
        self.expenses.append(self.expense)
        return self.expenses

    def view_expenses(self):
        if not self.expense:
            print("No Expenses Yet")

        else:
            for expense in self.expenses:
                print(f"\nName = {expense["Name"]} | Amount = {expense["Amount"]} | Category = {expense["Category"]}")

    def total_spendings(self):
        total = 0
        for expense in self.expenses:
            total += expense["Amount"]
        print(f"\nTotal = {total}")

tracker = ExpenseTracker()
tracker.add_expense("Car", 8000000, "Vehicle")
tracker.add_expense("Table", 8000, "Furniture")
tracker.view_expenses()
tracker.total_spendings()