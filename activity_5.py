
units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 2
    print("Electricity Bill:", bill)
elif units <= 200:
    bill = 200 + (units - 100) * 3
    print("Electricity Bill:", bill)
else:
    bill = 500 + (units - 200) * 5
    print("Electricity Bill:", bill)
