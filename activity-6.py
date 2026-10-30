
marks1 = int(input("Enter first exam marks: "))
marks2 = int(input("Enter second exam marks: "))

if marks1 < 0 or marks1 > 100 or marks2 < 0 or marks2 > 100:
    print("Invalid marks")
elif marks2 > marks1:
    print("Performance Improved")
elif marks2 < marks1:
    print("Performance Declined")
else:
    print("No Change")
