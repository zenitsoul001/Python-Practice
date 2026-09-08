style = "="*50
q1 = f"{style}\n1. What is the capital of India?\n    (a) Mumbai\n    (b) New Delhi\n    (c) Kolkata\n    (d) Chennai"
q2 = f"{style}\n2. Which is the largest planet in our solar system?\n    (a) Earth\n    (b) Mars\n    (c) Saturn\n    (d) Jupiter"
q3 = f"{style}\n3. How many days are there in a leap year?\n    (a) 365\n    (b) 364\n    (c) 366\n    (d) 360"

score = 0

def quiz(score):
    questions =[q1,q2,q3]
    for question in questions:
        print(question)
        user_inp = input("Enter your Answer: ").lower()
        if question == q1 and user_inp == "b":
                score += 1
                print(f"Correct answer Your score is now {score}")

        elif question == q2 and user_inp == "d":
                score += 1
                print(f"Correct answer Your score is now {score}")
  
        elif question == q3 and user_inp == "c":
                score += 1
                print(f"Correct answer Your score is now {score}")
        else:
            print("Wrong Answer!")

    return f"Your Total Score from 3 is {score}"

print(quiz(score))