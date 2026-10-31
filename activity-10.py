

key = input("Enter correct answers: ")
answers = input("Enter student answers: ")

if len(key) != len(answers):
    print("Invalid answers")
else:
    score = 0

    for i in range(len(key)):
        if key[i] == answers[i]:
            score = score + 1

    print("Total Questions:", len(key))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(key) - score)

    if score >= len(key) / 2:
        print("Good Performance")
    else:
        print("Needs Improvement")

