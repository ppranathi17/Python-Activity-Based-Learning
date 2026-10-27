
    marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 35:
    print("Pass")
elif marks >= 32:
    marks = marks + 3
    print("Pass with grace marks:", marks)
else:
    print("Fail")
    
