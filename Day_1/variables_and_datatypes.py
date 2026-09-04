# ==========================================
# PRACTICE 01: Variables and Basic Data Types
# ==========================================


# ------------------------------------------
# 1. VARIABLES
# ------------------------------------------

# Variable ek container ki tarah hota hai jo value ko store karta hai
student_name = "Gagandeep"
student_age = 24
course_fee = 15000.50
is_enrolled = True

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Course Fee:", course_fee)
print("Enrolled:", is_enrolled)


# ------------------------------------------
# 2. STRINGS (str)
# ------------------------------------------

# String ka use text store karne ke liye hota hai
first_name = "Gagan"
last_name = "Deep"

# Do strings ko + se combine kar sakte hain
full_name = first_name + " " + last_name

print("\nFull Name:", full_name)

# f-string se variables ko sentence mein use kar sakte hain
print(f"My name is {full_name}.")

# String ke characters ki total sankhya
print("Name Length:", len(full_name))

# String ko uppercase aur lowercase mein convert karna
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())


# ------------------------------------------
# 3. INTEGERS AND FLOATS
# ------------------------------------------

# Integer mein bina decimal wale numbers store hote hain
number_of_students = 25

# Float mein decimal wale numbers store hote hain
price_per_student = 499.50

# Multiplication karke total amount calculate kar rahe hain
total_amount = number_of_students * price_per_student

print("\nNumber of Students:", number_of_students)
print("Price Per Student:", price_per_student)
print("Total Amount:", total_amount)

# Basic mathematical operations
number_one = 20
number_two = 6

print("Addition:", number_one + number_two)
print("Subtraction:", number_one - number_two)
print("Multiplication:", number_one * number_two)
print("Division:", number_one / number_two)
print("Floor Division:", number_one // number_two)
print("Remainder:", number_one % number_two)
print("Power:", number_one ** 2)


# ------------------------------------------
# 4. BOOLEANS (bool)
# ------------------------------------------

# Boolean ke paas sirf do values hoti hain: True ya False
has_passport = True
has_ielts = False

print("\nHas Passport:", has_passport)
print("Has IELTS:", has_ielts)

age = 19

# Comparison ka result hamesha True ya False hota hai
is_adult = age >= 18

print("Is Adult:", is_adult)

# and ka matlab hai dono conditions True honi chahiye
can_apply = has_passport and has_ielts

print("Can Apply:", can_apply)


# ------------------------------------------
# 5. LIST
# ------------------------------------------

# List mein multiple values store hoti hain
# List ordered aur changeable hoti hai
countries = ["Canada", "UK", "Germany", "Australia"]

print("\nComplete List:", countries)

# Index counting 0 se start hoti hai
print("First Country:", countries[0])
print("Second Country:", countries[1])

# List mein nayi value add karna
countries.append("New Zealand")

print("After Adding Country:", countries)

# List ki value change karna
countries[1] = "United Kingdom"

print("After Changing Country:", countries)

# List se value remove karna
countries.remove("Germany")

print("After Removing Country:", countries)


# ------------------------------------------
# 6. TUPLE
# ------------------------------------------

# Tuple bhi multiple values store karta hai
# Lekin tuple banne ke baad uski values change nahi kar sakte
week_days = ("Monday", "Tuesday", "Wednesday")

print("\nComplete Tuple:", week_days)
print("First Day:", week_days[0])

# Yeh error dega kyunki tuple changeable nahi hota
# week_days[0] = "Sunday"


# ------------------------------------------
# 7. SET
# ------------------------------------------

# Set unique values store karta hai
# Duplicate values automatically remove ho jaati hain
skills = {"Python", "HTML", "CSS", "Python"}

print("\nSkills Set:", skills)

# Set mein nayi value add karna
skills.add("JavaScript")

print("After Adding Skill:", skills)

# Set ka order fixed nahi hota
# Isliye output ka order change ho sakta hai


# ------------------------------------------
# 8. DICTIONARY
# ------------------------------------------

# Dictionary data ko key-value pairs mein store karti hai
student = {
    "name": "Gagandeep",
    "age": 24,
    "course": "Python",
    "is_enrolled": True
}

print("\nComplete Dictionary:", student)

# Dictionary ki particular value access karna
print("Student Name:", student["name"])
print("Student Course:", student["course"])

# Existing value update karna
student["age"] = 25

# Nayi key aur value add karna
student["city"] = "Ludhiana"

print("Updated Dictionary:", student)


# ------------------------------------------
# 9. CHECKING DATA TYPES
# ------------------------------------------

# type() se pata chalta hai ki variable ka data type kya hai
print("\nData Types:")
print(type(student_name))         # String: str
print(type(student_age))          # Integer: int
print(type(course_fee))           # Float: float
print(type(is_enrolled))          # Boolean: bool
print(type(countries))            # List: list
print(type(week_days))            # Tuple: tuple
print(type(skills))               # Set: set
print(type(student))              # Dictionary: dict