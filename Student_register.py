import random

print("\nSTUDENT REGISTER")
student_details = []   
questions = ["12 * 12 >> ","90 // 10 >> ","A cat has 2 ears >> ","A car has how many wheels >> ",
            "The sky is blue. >> ","Fish can fly. >> ","2 + 2 equals 4.","Water boils at 100 degrees Celsius.",
            "Cats are reptiles.","Earth is the third planet from the sun."]
answers = ["144","9","TRUE","4","TRUE","FASLE","TRUE","TRUE","FALSE","TRUE"]

for i in range(10):
    user_name = input('\nname: ').capitalize()
    user_username = input('username: ').capitalize()
    user_score = 0
    print("Practice Questions >> \n")
    for i in range(4):
        question = random.choice(questions)
        print(question)
        user_answer = input("input your answer >> ").upper()
        for i, quest in enumerate(questions):
            if question == quest:
                if user_answer == answers[i] :
                    print("correct")
                    user_score += 25
                else: 
                    print("wrong")
                break
    print(f"user score = {user_score}")
    student_details.append([user_name, user_username, user_score])
    proceed = input("\nRegister new student Y/N >> ")
    if proceed.upper() == "N":
        print("Done")
        print("---------------------------------")
        for student_record in student_details:
            print(f"{student_record[0]} score is {student_record[-1]}")
        print("---------------------------------")
        break
    elif proceed.upper() != "Y":
        print("Invalid input ; session terminated\n")
        print("---------------------------------")
        for student_record in student_details:
            print(f"{student_record[0]} score is {student_record[-1]}")
        print("---------------------------------")
        break






