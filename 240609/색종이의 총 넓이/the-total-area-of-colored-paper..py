# number of colored papers
n = int(input())

# offset 
offset = 100
maxRange = offset * 2
checklist = [
    [0 for _ in range(maxRange + 1)] for _ in range(maxRange + 1)
]

# calculation
for _ in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 8, y1 + 8

    for r in range(x1, x2):
        for c in range(y1, y2):
            checklist[r][c] = 1

# count
totalArea = 0
for r in range(len(checklist)):
    for c in range(len(checklist)):
        if checklist[r][c] == 1:
            totalArea += 1

# print
print(totalArea)