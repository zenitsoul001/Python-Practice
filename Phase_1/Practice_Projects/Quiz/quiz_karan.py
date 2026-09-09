from questions import * 

score = 0
def quiz_master(question,corr_opt,design):
        global score

        while(True):
                print(f"{design}\n{question}\n{design}\n")
                user_inp = input("Enter the input between a/b/c/d : ").lower()
                if user_inp not in ["a","b","c","d"]:
                        print("Plz provide a valid Input\n")
                        continue
                elif user_inp == corr_opt:
                        score += 1
                        print(f"\nCorrect! and your Score is {score}\n")
                        break
                else:
                        print("\nIncorrect\n!")
                        continue

All_Questions = [
    question1, question2, question3, question4,
    question5, question6, question7, question8,
    question9, question10, question11, question12
]                 

x = input("Enter the design: ")
des = x * 50
for i in All_Questions:
        quiz_master(i[0],i[1],des)





