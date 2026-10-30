
balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Remaining balance:", balance)
