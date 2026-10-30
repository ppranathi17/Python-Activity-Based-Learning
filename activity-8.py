
n = int(input("Enter number of readings: "))
total = 0

if n <= 0:
    print("Invalid input")
else:
    for i in range(n):
        temp = float(input("Enter temperature: "))
        total = total + temp

    average = total / n

    print("Average Temperature:", average)

    if average > 35:
        print("High Temperature")
    else:
        print("Normal Temperature")
