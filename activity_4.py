
distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage in km per litre: "))
price = float(input("Enter fuel price per litre: "))

if distance < 0 or mileage <= 0 or price < 0:
    print("Invalid input")
else:
    fuel = distance / mileage
    cost = fuel * price

    print("Fuel required:", fuel, "litres")
    print("Total fuel cost:", cost)
