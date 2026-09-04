# ==========================================
# PRACTICE 04: FUNCTIONS
# ==========================================

# Function reusable code ka ek block hota hai
# Function ko "def" keyword se create kiya jata hai
# Function tabhi chalega jab hum use call karenge


# ------------------------------------------
# 1. CREATING A SIMPLE FUNCTION
# ------------------------------------------

def show_message():
    # Yeh code function call hone par chalega
    print("Welcome to Python Practice!")


# Function ko call kar rahe hain
show_message()
show_message()


# ------------------------------------------
# 2. FUNCTION WITH ONE PARAMETER
# ------------------------------------------

# "name" ek parameter hai
# Parameter function ke andar information receive karta hai
def greet_student(name):
    print(f"Hello {name}, welcome to Python!")


# "Gagandeep" aur "Aman" arguments hain
# Argument actual value hoti hai jo function ko pass ki jaati hai
greet_student("Gagandeep")
greet_student("Aman")


# ------------------------------------------
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ------------------------------------------

def show_student_details(name, age, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# Values same order mein parameters ko milengi
show_student_details("Gagandeep", 24, "Python")


# ------------------------------------------
# 4. FUNCTION RETURNING A VALUE
# ------------------------------------------

def add_numbers(number_one, number_two):
    total = number_one + number_two

    # return result ko function ke bahar bhejta hai
    return total


# Returned value ko result variable mein store kar rahe hain
result = add_numbers(10, 5)

print("\nAddition Result:", result)


# ------------------------------------------
# 5. PRINT AND RETURN DIFFERENCE
# ------------------------------------------

def multiply_numbers(number_one, number_two):
    result = number_one * number_two
    return result


# Function ka returned result variable mein store kar sakte hain
multiplication_result = multiply_numbers(5, 4)

# Returned result ko aage calculation mein bhi use kar sakte hain
final_result = multiplication_result + 10

print("Multiplication Result:", multiplication_result)
print("Final Result:", final_result)


# ------------------------------------------
# 6. CALCULATE PERCENTAGE
# ------------------------------------------

def calculate_percentage(obtained_marks, total_marks):
    percentage = (obtained_marks / total_marks) * 100
    return percentage


student_percentage = calculate_percentage(420, 500)

print(f"\nStudent Percentage: {student_percentage}%")


# ------------------------------------------
# 7. RETURNING RESULT USING CONDITIONS
# ------------------------------------------

def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


student_result = check_result(65)

print("Student Result:", student_result)


# ------------------------------------------
# 8. DEFAULT ARGUMENT
# ------------------------------------------

# country ki default value "Germany" hai
def create_application(student_name, country="Germany"):
    print(f"{student_name} is applying for {country}.")


# Country pass nahi ki, isliye default value Germany use hogi
create_application("Gagandeep")

# Country pass ki, isliye Canada use hoga
create_application("Aman", "Canada")

# Required parameters hamesha default parameters se pehle likhe jaate hain
# Correct:   def example(name, country="Germany")
# Incorrect: def example(country="Germany", name)


# ------------------------------------------
# 9. KEYWORD ARGUMENTS
# ------------------------------------------

def display_profile(name, age, course):
    print("\nStudent Profile")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# Keyword arguments mein parameter ka naam mention karte hain
# Isliye arguments ka order change kar sakte hain
display_profile(
    course="Python",
    name="Gagandeep",
    age=24
)


# ------------------------------------------
# 10. POSITIONAL AND KEYWORD ARGUMENTS
# ------------------------------------------

def calculate_fee(student_name, course_fee, discount=0):
    final_fee = course_fee - discount

    print(f"\nStudent Name: {student_name}")
    print(f"Original Fee: ₹{course_fee}")
    print(f"Discount: ₹{discount}")
    print(f"Final Fee: ₹{final_fee}")

    return final_fee


# Gagandeep aur 15000 positional arguments hain
# discount keyword argument hai
payable_fee = calculate_fee(
    "Gagandeep",
    15000,
    discount=2000
)

print("Payable Fee:", payable_fee)


# ------------------------------------------
# 11. PRACTICAL EXAMPLE: ELIGIBILITY CHECK
# ------------------------------------------

# IELTS ki default requirement 6.0 rakhi hai
def check_eligibility(percentage, ielts_score, required_ielts=6.0):

    if percentage < 60:
        return "Not eligible: Academic percentage is low."

    elif ielts_score < required_ielts:
        return "Not eligible: IELTS score is low."

    else:
        return "Student is eligible to apply."


application_result = check_eligibility(
    percentage=72,
    ielts_score=6.5
)

print("\nApplication Result:", application_result)


# ------------------------------------------
# 12. FUNCTION CALLING ANOTHER FUNCTION
# ------------------------------------------

def calculate_total(price, quantity):
    return price * quantity


def generate_bill(price, quantity):
    total = calculate_total(price, quantity)
    print(f"\nPrice: ₹{price}")
    print("Quantity:", quantity)
    print(f"Total Bill: ₹{total}")


generate_bill(499, 10)