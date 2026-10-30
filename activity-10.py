passengers = [100, 80, 60]
capacity = 40

for i in range(len(passengers)):
    buses = passengers[i] // capacity

    if passengers[i] % capacity != 0:
        buses = buses + 1

    served = buses * capacity
    unserved = max(0, passengers[i] - served)

    print("Route", i + 1)
    print("Number of buses:", buses)
    print("Unserved passengers:", unserved)