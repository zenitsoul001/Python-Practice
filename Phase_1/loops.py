# ==========================================
# PRACTICE 03: LOOPS
# ==========================================

# Loops ka use same code ko multiple times chalane ke liye hota hai


# ------------------------------------------
# 1. BASIC FOR LOOP
# ------------------------------------------

countries = ["Canada", "UK", "Germany", "Australia"]

# For loop list ki har value ko one-by-one access karega
for country in countries:
    print(country)


# ------------------------------------------
# 2. FOR LOOP WITH RANGE
# ------------------------------------------

print("\nNumbers from 1 to 5:")

# range(1, 6) mein 1 included hai, lekin 6 included nahi hai
for number in range(1, 6):
    print(number)


# ------------------------------------------
# 3. RANGE WITH STEP
# ------------------------------------------

print("\nEven numbers:")

# range(start, stop, step)
# Loop 2 se start hoga aur har baar 2 ka jump karega
for number in range(2, 11, 2):
    print(number)


# ------------------------------------------
# 4. FOR LOOP WITH A DICTIONARY
# ------------------------------------------

student = {
    "name": "Gagandeep",
    "course": "Python",
    "city": "Ludhiana"
}

print("\nStudent Details:")

# items() dictionary ki key aur value dono deta hai
for key, value in student.items():
    print(f"{key}: {value}")


# ------------------------------------------
# 5. BASIC WHILE LOOP
# ------------------------------------------

count = 1

# Jab tak condition True rahegi, loop chalta rahega
while count <= 5:
    print("Count:", count)

    # Har iteration mein count ko 1 se increase karna zaroori hai
    count += 1

# Agar count increase nahi karenge to infinite loop ban sakta hai


# ------------------------------------------
# 6. BREAK WITH FOR LOOP
# ------------------------------------------

print("\nBreak Example:")

for number in range(1, 11):

    # Jab number 6 hoga to complete loop stop ho jayega
    if number == 6:
        print("Number 6 found. Loop stopped!")
        break

    print(number)


# ------------------------------------------
# 7. BREAK WITH WHILE LOOP
# ------------------------------------------

attempt = 1

while attempt <= 5:
    print("Login Attempt:", attempt)

    # Third attempt par loop ko completely stop kar rahe hain
    if attempt == 3:
        print("Login successful!")
        break

    attempt += 1


# ------------------------------------------
# 8. CONTINUE WITH FOR LOOP
# ------------------------------------------

print("\nContinue Example:")

for number in range(1, 11):

    # Agar number 5 hai to current iteration skip ho jayegi
    if number == 5:
        continue

    print(number)

# Output mein 5 print nahi hoga, lekin loop aage chalta rahega


# ------------------------------------------
# 9. PRINT ONLY ODD NUMBERS
# ------------------------------------------

print("\nOdd Numbers:")

for number in range(1, 11):

    # Agar number even hai to us iteration ko skip kar do
    if number % 2 == 0:
        continue

    print(number)


# ------------------------------------------
# 10. CONTINUE WITH WHILE LOOP
# ------------------------------------------

number = 0

while number < 10:
    # Continue se pehle number increase karna zaroori hai
    number += 1

    # Even numbers ko skip kar rahe hain
    if number % 2 == 0:
        continue

    print("Odd Number:", number)


# ------------------------------------------
# 11. PRACTICAL EXAMPLE: SEARCH STUDENT
# ------------------------------------------

students = ["Aman", "Rahul", "Gagandeep", "Simran"]
student_to_find = "Gagandeep"

for student_name in students:

    print("Checking:", student_name)

    # Student milte hi loop stop ho jayega
    if student_name == student_to_find:
        print(f"{student_to_find} found!")
        break


# ------------------------------------------
# 12. SIMPLE MULTIPLICATION TABLE
# ------------------------------------------

table_number = 5

print(f"\nTable of {table_number}:")

for number in range(1, 11):
    result = table_number * number
    print(f"{table_number} x {number} = {result}")