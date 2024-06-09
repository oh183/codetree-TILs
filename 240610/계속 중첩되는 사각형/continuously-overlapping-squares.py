n = int(input())

offset = 100
MaxRange = 2 * offset
checkList = [
    [0 for _ in range(MaxRange + 1)] for _ in range(MaxRange + 1)
]

for i in range(n):
    if i % 2 == 0:
        color = "Red"
    else:
        color = "Blue"
    
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for r in range(x1, x2):
        for c in range(y1, y2):
            checkList[r][c] = color

totalArea = 0
for r in range(len(checkList)):
    for c in range(len(checkList)):
        if checkList[r][c] == "Blue":
            totalArea += 1

print(totalArea)