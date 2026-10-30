registrations = [
    ("Ram", "Python"),
    ("Sam", "Java"),
    ("Ram", "Python"),
    ("Ravi", "Python")
]

print("Duplicate Registrations:")

for i in range(len(registrations)):
    for j in range(i + 1, len(registrations)):
        if registrations[i] == registrations[j]:
            print(registrations[i])

print("Invalid Registrations:")

for student, course in registrations:
    if course not in ("Python", "Java"):
        print(student, course)