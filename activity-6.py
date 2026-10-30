
electricity = int(input("Enter electricity units: "))
water = int(input("Enter water units: "))

if electricity < 0 or water < 0:
    print("Invalid input")
else:
    e_bill = electricity * 5
    w_bill = water * 2

    total = e_bill + w_bill

    print("Electricity Bill:", e_bill)
    print("Water Bill:", w_bill)
    print("Total Bill:", total)

    if electricity > 200:
        print("High Electricity Usage")
    else:
        print("Normal Electricity Usage")

