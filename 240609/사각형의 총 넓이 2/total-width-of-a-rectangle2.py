# input
n = int(input())
offset = 100

# create 2d array
arr = [
    [0 for _ in range(200)] for _ in range(200)
]

# calculation (Reminder -> (x1,y1), (x2, y2) -> (x1,y1), (x2-1, y2-1))
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset,  x2 + offset, y2 + offset

    for r in range(x1, x2):
        for c in range(y1, y2):
            arr[r][c] = 1

# counting
totalArea = 0 
for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] > 0:
            totalArea += 1

# print
print(totalArea)