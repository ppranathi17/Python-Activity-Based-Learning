teams = ["Team A", "Team B", "Team C"]
points = [6, 3, 6]

for i in range(3):
    for j in range(i + 1, 3):
        if points[i] < points[j]:
            points[i], points[j] = points[j], points[i]
            teams[i], teams[j] = teams[j], teams[i]

print("Tournament Rankings")

for i in range(3):
    print(i + 1, teams[i], points[i], "points")