expenses = []
expense = {}

print("""===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
3. View total spending
4. Exit""")

def add_exp(name,amount,category):
    global expense,expenses
    expense["Name"] = name
    expense["Amount"] = amount
    expense["Category"] = category
    expenses.append(expense)
    return expenses


inp_name = input("Enter the Name : ")
inp_amount = input("Enter the amount : ")
inp_category = input("Enter the category : ")

print(add_exp(inp_name,inp_amount,inp_category))