# ==========================================
# PRACTICE 05: ERROR HANDLING
# ==========================================

# Error handling se program error aane par suddenly crash nahi hota
#
# try     = risky code yahan likhte hain
# except  = error aane par yeh code chalega
# else    = error na aane par yeh code chalega
# finally = error aaye ya na aaye, yeh hamesha chalega


# ------------------------------------------
# 1. BASIC TRY AND EXCEPT
# ------------------------------------------

try:
    number = 10 / 0
    print(number)

except ZeroDivisionError:
    # Kisi number ko zero se divide nahi kar sakte
    print("Error: Number ko zero se divide nahi kar sakte.")


# ------------------------------------------
# 2. HANDLING INVALID USER INPUT
# ------------------------------------------

try:
    # input() string deta hai
    # int() us string ko integer mein convert karta hai
    age = int(input("\nEnter your age: "))

    print("Your age is:", age)

except ValueError:
    # Agar user number ki jagah text enter karega to yeh chalega
    print("Error: Please enter age in numbers only.")


# ------------------------------------------
# 3. MULTIPLE EXCEPT BLOCKS
# ------------------------------------------

try:
    first_number = int(input("\nEnter first number: "))
    second_number = int(input("Enter second number: "))

    result = first_number / second_number
    print("Division Result:", result)

except ValueError:
    # Yeh error tab aayega jab input valid number nahi hoga
    print("Error: Dono values valid numbers honi chahiye.")

except ZeroDivisionError:
    # Yeh error tab aayega jab second number zero hoga
    print("Error: Zero se division allowed nahi hai.")


# ------------------------------------------
# 4. TRY, EXCEPT AND ELSE
# ------------------------------------------

try:
    marks = float(input("\nEnter your marks: "))

except ValueError:
    print("Error: Marks numbers mein enter karein.")

else:
    # Else sirf tab chalega jab try mein koi error nahi aayega
    if 0 <= marks <= 100:
        print("Valid marks entered:", marks)
    else:
        print("Marks 0 se 100 ke beech hone chahiye.")


# ------------------------------------------
# 5. TRY, EXCEPT AND FINALLY
# ------------------------------------------

try:
    course_fee = float(input("\nEnter course fee: "))
    students = int(input("Enter number of students: "))

    fee_per_student = course_fee / students
    print("Fee Per Student:", fee_per_student)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Number of students zero nahi ho sakta.")

finally:
    # Finally error aaye ya na aaye, hamesha execute hota hai
    print("Fee calculation process completed.")


# ------------------------------------------
# 6. COMPLETE EXAMPLE
# ------------------------------------------

try:
    percentage = float(input("\nEnter percentage: "))
    ielts_score = float(input("Enter IELTS score: "))

    # Agar entered value expected range mein nahi hai
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage 0 se 100 ke beech honi chahiye.")

    if ielts_score < 0 or ielts_score > 9:
        raise ValueError("IELTS score 0 se 9 ke beech hona chahiye.")

except ValueError as error:
    # "as error" se actual error message milta hai
    print("Invalid information:", error)

else:
    # Yeh block tab chalega jab koi error nahi aaya
    if percentage >= 60 and ielts_score >= 6:
        print("Student is eligible to apply.")
    else:
        print("Student does not meet the requirements.")

finally:
    # Yeh block har situation mein chalega
    print("Eligibility check completed.")


# ------------------------------------------
# 7. ERROR HANDLING INSIDE A FUNCTION
# ------------------------------------------

def calculate_percentage(obtained_marks, total_marks):
    try:
        percentage = (obtained_marks / total_marks) * 100

    except ZeroDivisionError:
        return "Error: Total marks zero nahi ho sakte."

    except TypeError:
        return "Error: Marks numbers mein hone chahiye."

    else:
        return f"Percentage: {percentage:.2f}%"

    finally:
        print("Percentage calculation function executed.")


print("\n", calculate_percentage(420, 500))
print("\n", calculate_percentage(420, 0))
print("\n", calculate_percentage("420", 500))