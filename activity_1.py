n = int(input("Enter number of subjects: "))
total = 0
failed = False

for i in range(n):
    marks = int(input("Enter marks: "))

    if 30 <= marks < 35:
        marks = 35
        print("Grace marks added")

    if marks < 35:
        print("Fail")
        failed = True
    else:
        print("Pass")

    total += marks

print("Total marks:", total)
percentage = total / n
print("Percentage:", percentage, "%")

if failed:
    print("Final Result: Fail")
elif percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
else:
    print("Pass")