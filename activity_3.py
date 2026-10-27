
held = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid input")
else:
    percentage = attended / held * 100
    print("Attendance:", percentage, "%")

    if percentage >= 75:
        print("Eligible for exams")
    else:
        print("Not eligible for exams")
