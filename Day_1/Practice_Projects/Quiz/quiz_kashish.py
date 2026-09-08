# quiz_questions = {
#     "What is the capital of France?": "Paris",
#     "What is 2 + 2?": "4",
#     "What is the largest planet in our solar system?": "Jupiter",
#     "What is the chemical symbol for water?": "H2O",
#     "What is the capital of Italy?": "Rome",
#     "What is the square root of 16?": "4",
#     "What is the currency of Japan?": "Yen",
#     "What is the largest ocean on Earth?": "Pacific Ocean",
#     "What is the capital of Australia?": "Canberra",
#     "What is the chemical symbol for gold?": "Au",
#     "What is the capital of Canada?": "Ottawa",
#     "What is the largest desert in the world?": "Sahara",
#     "What is the capital of Germany?": "Berlin",
#     "What is the capital of India?": "New Delhi",
#     "Which is the largest planet in our solar system?": "Jupiter",
#     "How many days are there in a leap year?": "366"
# }

score = 0
correct_answers = 0
incorrect_answers = 0
user_input = input("1. What is the capital of France?\n   (a) Berlin\n   (b) Paris\n   (c) Madrid\n   (d) Rome\n Enter the correct option: ").lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")
    
user_input = input("2. What is 2 + 2?\n   (a) 3\n   (b) 5\n   (c) 4\n   (d) 6\n Enter the correct option: ").lower()
if user_input == 'c':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("3. What is the largest planet in our solar system?\n   (a) Earth\n   (b) Saturn\n   (c) Mars\n   (d) Jupiter\n Enter the correct option: ").lower()
if user_input == 'd':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'c']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("4. What is the chemical symbol for water?\n   (a) CO2\n   (b) H2O\n   (c) O2\n   (d) NaCl\n Enter the correct option: ").lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("5. What is the capital of Italy?\n   (a) Milan\n   (b) Venice\n   (c) Rome\n   (d) Naples\n Enter the correct option: ").lower()
if user_input == 'c':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("6. What is the square root of 16?\n   (a) 2\n   (b) 4\n   (c) 6\n   (d) 8\n Enter the correct option: ").lower().lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("7. What is the currency of Japan?\n   (a) Dollar\n   (b) Won\n   (c) Yen\n   (d) Euro\n Enter the correct option: ").lower()
if user_input == 'c':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("8. What is the largest ocean on Earth?\n   (a) Atlantic Ocean\n   (b) Indian Ocean\n   (c) Arctic Ocean\n   (d) Pacific Ocean\n Enter the correct option: ").lower()
if user_input == 'd':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'c']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")


user_input = input("9. What is the capital of Australia?\n   (a) Sydney\n   (b) Melbourne\n   (c) Canberra\n   (d) Perth\n Enter the correct option: ").lower()
if user_input == 'c':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("10. What is the chemical symbol for gold?\n   (a) Ag\n   (b) Au\n   (c) Fe\n   (d) Go\n Enter the correct option: ").lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("11. What is the capital of Canada?\n   (a) Toronto\n   (b) Vancouver\n   (c) Ottawa\n   (d) Montreal\n Enter the correct option: ").lower()
if user_input == 'c':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("12. What is the largest hot desert in the world?\n   (a) Gobi Desert\n   (b) Sahara Desert\n   (c) Arabian Desert\n   (d) Kalahari Desert\n Enter the correct option: ").lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("13. What is the capital of Germany?\n   (a) Munich\n   (b) Frankfurt\n   (c) Hamburg\n   (d) Berlin\n Enter the correct option: ").lower()
if user_input == 'd':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'b', 'c']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

user_input = input("14. What is the capital of India?\n   (a) Mumbai\n   (b) New Delhi\n   (c) Kolkata\n   (d) Chennai\n Enter the correct option: ").lower()
if user_input == 'b':
    print("Correct!")
    score += 1
    correct_answers += 1
elif user_input in ['a', 'c', 'd']:
    print("Incorrect!")
    incorrect_answers += 1
else:
    print("Invalid option! Please enter a, b, c, or d.")

print(f"\nYour final score is: {score}/14")
print(f"Correct answers: {correct_answers}")
print(f"Incorrect answers: {incorrect_answers}")