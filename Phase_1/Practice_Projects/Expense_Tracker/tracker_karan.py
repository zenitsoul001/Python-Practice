expenses = []
expense = {}
design = "=" * 10

def add_exp():
    print(f"{design} Fill these details. {design}")
    name = input("  Enter the Name : ")
    flag = True
    while(flag):
        try:
            amount = float(input("  Enter the amount : "))
            flag = False
        except ValueError:
            print("\n-------------------\nEnter the Numeric value for Amount!\n-------------------\n")
        continue
    category = input("  Enter the category : ")
    expense = {
        "Name": name,
        "Amount": amount,
        "Category": category
    }
    expenses.append(expense)
    print("Expense Added succesfully!\n")

def view_exp():
    if not expenses:
        print("No expenses added yet.")
        return
    print(f"{design} Total Expenses : {len(expenses)} {design}")
    for expense in expenses:
        print(f"Name: {expense['Name']}")
        print(f"Amount: ₹{expense['Amount']:.2f}")
        print(f"Category: {expense['Category']}")
        print(design*2)

def view_total_exp():
    total = 0
    for expense in expenses:
        total += expense["Amount"]

    print(f"Total is : {total}")

def exit_exp():
    print("Thanks for using the Expense Tracker!")


while(True):
    print("""\n===== EXPENSE TRACKER =====    
    1. Add expense
    2. View all expenses
    3. View total spending
    4. Exit""")
    try:
        user_inp = int(input("  Enter Your Choice: "))
    except ValueError:
        print("Provide valid Input between 1/2/3/4 ")
        continue
    if user_inp == 1:
        add_exp()
    elif user_inp == 2:
        view_exp()
    elif user_inp == 3:
        view_total_exp()
    elif user_inp == 4:
        exit_exp()
        break
