
consultation = float(input("Enter consultation charge: "))
treatment = float(input("Enter treatment charge: "))

if consultation < 0 or treatment < 0:
    print("Invalid input")
else:
    total = consultation + treatment

    if total >= 5000:
        total = total - 500

    print("Final Bill:", total)
