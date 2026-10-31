

distance = float(input("Enter distance in km: "))
category = input("Enter category (student/normal): ")

if distance <= 0:
    print("Invalid distance")
elif category == "student":
    fare = distance * 1
    print("Student Fare:", fare)
elif category == "normal":
    fare = distance * 2
    print("Normal Fare:", fare)
else:
    print("Invalid category")

