

students = int(input("Enter number of students: "))
fee = int(input("Enter registration fee per student: "))
sponsorship = int(input("Enter sponsorship amount: "))
expenses = int(input("Enter total expenses: "))

if students < 0 or fee < 0 or sponsorship < 0 or expenses < 0:
    print("Invalid input")
else:
    registration = students * fee
    total = registration + sponsorship
    balance = total - expenses

    print("Registration Amount:", registration)
    print("Total Funds:", total)
    print("Final Balance:", balance)

    if balance >= 0:
        print("Festival is in Profit")
    else:
        print("Festival is in Loss")
