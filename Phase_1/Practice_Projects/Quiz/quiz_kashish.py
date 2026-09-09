quiz_questions = [("1. What is the capital of France?\n   (a) Berlin\n   (b) Paris\n   (c) Madrid\n   (d) Rome ", "b"),
                  ("2. What is 2 + 2?\n   (a) 3\n   (b) 5\n   (c) 4\n   (d) 6\n ", "c"),
                  ("3. What is the largest planet in our solar system?\n   (a) Earth\n   (b) Saturn\n   (c) Mars\n   (d) Jupiter ", "d"),
                  ("4. What is the chemical symbol for water?\n   (a) CO2\n   (b) H2O\n   (c) O2\n   (d) NaCl ", "b"),
                  ("5. What is the capital of Italy?\n   (a) Milan\n   (b) Venice\n   (c) Rome\n   (d) Naples ", "c"),
                  ("6. What is the square root of 16?\n   (a) 2\n   (b) 4\n   (c) 6\n   (d) 8 ", "b"),
                  ("7. What is the currency of Japan?\n   (a) Dollar\n   (b) Won\n   (c) Yen\n   (d) Euro ", "c"),
                  ("8. What is the largest ocean on Earth?\n   (a) Atlantic Ocean\n   (b) Indian Ocean\n   (c) Arctic Ocean\n   (d) Pacific Ocean ", "d"),
                  ("9. What is the capital of Australia?\n   (a) Sydney\n   (b) Melbourne\n   (c) Canberra\n   (d) Perth ", "c"),
                  ("10. What is the chemical symbol for gold?\n   (a) Ag\n   (b) Au\n   (c) Fe\n   (d) Go ", "b"),
                  ("11. What is the capital of Canada?\n   (a) Toronto\n   (b) Vancouver\n   (c) Ottawa\n   (d) Montreal ", "c"),
                  ("12. What is the largest hot desert in the world?\n   (a) Gobi Desert\n   (b) Sahara Desert\n   (c) Arabian Desert\n   (d) Kalahari Desert ", "b"),
                  ("13. What is the capital of Germany?\n   (a) Munich\n   (b) Frankfurt\n   (c) Hamburg\n   (d) Berlin ", "d"),
                  ("14. What is the capital of India?\n   (a) Mumbai\n   (b) New Delhi\n   (c) Kolkata\n   (d) Chennai ", "b")]
score = 0
correct_answers = 0
incorrect_answers = 0

def ask_question(question, correct_option):
    global score, correct_answers, incorrect_answers

    while True:
        user_input = input(question + "\nEnter the correct option: ").lower()

        if user_input not in ['a', 'b', 'c', 'd']:
            print("Invalid option! Please enter a, b, c, or d.\n")
            continue

        if user_input == correct_option:
            print("Correct!\n")
            score += 1
            correct_answers += 1
        else:
            print("Incorrect!\n")
            incorrect_answers += 1

        break

for question, correct_option in quiz_questions:
    print("-" * 50)
    ask_question(question, correct_option)
    print("-" * 50)

print("=" * 50)
print(f"Your final score is: {score}/14")
print(f"Correct answers: {correct_answers}")
print(f"Incorrect answers: {incorrect_answers}")
print("=" * 50)