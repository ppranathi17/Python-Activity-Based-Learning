
electricity = int(input("Enter electricity units: "))
water = int(input("Enter water units: "))

if electricity < 0 or water < 0:
    print("Invalid input")
else:
    total = electricity + water

    print("Total Consumption:", total)

    if electricity > 500:
        print("High Electricity Consumption")
    else:
        print("Normal Electricity Consumption")
