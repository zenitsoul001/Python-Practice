expenses = []
expense = {}

def add_expense(name, amount, category):
    expense = {
        "Name" : name,
        "Amount" : amount,
        "Category" : category
    }
    expenses.append(expense)
    return expenses

def view_expenses():
    if not expenses:
        print("No Expenses Added Yet")
    
    for expense in expenses:
        print(f"\nName : {expense['Name']} | Amount : {expense['Amount']} | Category : {expense['Category']}")

def total_spending():
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    return total

def exit_exp():
    print("Thank you for using the Expense Tracker. Goodbye!")

## Expense Tracker
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
        add_expense(name, amount, category)
        print("Expense Added Successfully!")

    elif user_inp == 2:
        view_expenses()

    elif user_inp == 3:
        print(f"Total Spending: {total_spending()}")

    elif user_inp == 4:
        exit_exp()
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.") 