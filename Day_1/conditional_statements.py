# ==========================================
# PRACTICE 02: Conditional Statements
# ==========================================

# Conditional statements ki help se program decisions leta hai
# Python mein condition ke baad colon (:) lagana zaroori hai
# Condition ke andar ka code indentation (spaces) ke saath likha jata hai


# ------------------------------------------
# 1. IF STATEMENT
# ------------------------------------------

age = 20

# Agar condition True hogi, tabhi andar wala code chalega
if age >= 18:
    print("You are eligible to vote.")

# Agar condition False hogi to kuch bhi print nahi hoga
if age < 18:
    print("You are not eligible to vote.")


# ------------------------------------------
# 2. IF-ELSE STATEMENT
# ------------------------------------------

marks = 65

# Agar marks 40 ya usse zyada hain to student pass hai
if marks >= 40:
    print("\nResult: Pass")
else:
    # Agar if condition False hogi to else ka code chalega
    print("\nResult: Fail")


# ------------------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# ------------------------------------------

percentage = 76

# Multiple conditions check karne ke liye elif use hota hai
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")

# Python conditions ko upar se neeche check karta hai
# Pehli True condition milne ke baad baaki conditions check nahi hoti


# ------------------------------------------
# 4. COMPARISON OPERATORS
# ------------------------------------------

number = 10

# == check karta hai ki dono values equal hain ya nahi
if number == 10:
    print("\nNumber is equal to 10.")

# != check karta hai ki dono values different hain ya nahi
if number != 5:
    print("Number is not equal to 5.")

# > ka matlab greater than
if number > 5:
    print("Number is greater than 5.")

# < ka matlab less than
if number < 20:
    print("Number is less than 20.")

# >= ka matlab greater than or equal to
if number >= 10:
    print("Number is greater than or equal to 10.")

# <= ka matlab less than or equal to
if number <= 10:
    print("Number is less than or equal to 10.")


# ------------------------------------------
# 5. LOGICAL OPERATORS
# ------------------------------------------

student_age = 22
has_passport = True
has_ielts = True

# and mein dono conditions True honi chahiye
if student_age >= 18 and has_passport:
    print("\nStudent is an adult and has a passport.")

# or mein kam se kam ek condition True honi chahiye
if has_passport or has_ielts:
    print("Student has at least one required document.")

# not Boolean value ko opposite kar deta hai
if not has_ielts:
    print("Student needs to take the IELTS exam.")
else:
    print("Student has completed the IELTS requirement.")


# ------------------------------------------
# 6. REAL-LIFE EXAMPLE: UNIVERSITY ELIGIBILITY
# ------------------------------------------

student_percentage = 72
ielts_score = 6.5

# Pehle percentage check hogi
if student_percentage >= 60:

    # Percentage eligible hone ke baad IELTS check hoga
    if ielts_score >= 6.0:
        print("\nStudent is eligible to apply.")
    else:
        print("\nPercentage is sufficient, but IELTS score is low.")

else:
    print("\nStudent does not meet the academic requirement.")


# ------------------------------------------
# 7. USER INPUT EXAMPLE
# ------------------------------------------

# input() se user se value li jaati hai
# int() input ko string se integer mein convert karta hai
user_age = int(input("\nEnter your age: "))

if user_age < 13:
    print("You are a child.")
elif user_age < 18:
    print("You are a teenager.")
elif user_age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")