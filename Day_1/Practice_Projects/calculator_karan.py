
def calculator():
        while(True):
            try:
                num1 = int(input("Enter the Number 1: "))
                num2 = int(input("Enter the Number 2: "))
                print(f"\n{"="*45}\n Choose the Operation you want to perform: \n{"="*45}\n(1) For Addition\n(2) For Subtraction\n(3) For Multiply\n(4) For Divide\n(5) For Floor Division\n(6) For Power\n(7) For Exit.")
                choice = int(input("Enter Your Choice: "))
                print("Enter the Integer Values only!")
                if choice == 1:
                    print( num1 + num2)
                elif choice == 2:
                    print( num1 - num2)
                elif choice == 3:
                    print( num1 * num2)
                elif choice == 4:
                    print( num1 / num2)
                elif choice == 5:
                    print( num1 // num2)
                elif choice == 6:
                    print( num1 ** num2)
                elif choice == 7:
                    print("Calculator closed!")
                    break
            except ValueError:
                print("Enter integer values only!")

            except ZeroDivisionError:
                print("Zero Division Error!")

calculator()
