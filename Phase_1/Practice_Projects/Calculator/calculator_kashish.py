def calculate():
    while(True):
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("\nEnter second number: "))
        operation = int(input(f"\n {"="*8} Choose Operation: {"="*8}\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Floor Division\n6. Power\n7. Exit\n {"="*40}\nEnter Your Choice from 1-7: "))

        if operation == 1:
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == 4:
            try:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("\nError: Division by zero is not allowed.")

        elif operation == 5:
            result = num1 % num2
            print(f"\nResult: {num1} % {num2} = {result}")

        elif operation == 6:
            result = num1 ** num2
            print(f"\nResult: {num1} ** {num2} = {result}")

        elif operation == 7:
            print("\nExiting the calculator. Goodbye!")
            return

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

calculate()