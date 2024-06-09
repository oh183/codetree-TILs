# 2d array
arr = [
    [0 for _ in range(2000)] for _ in range(2000)
]

# offset
offset = 1000

# Rectangle A, B
for _ in range(2): # total 3 rectangles
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    # 격자로 옮겨야 하니까, (x1,y1) (x2-1, y2-1)
    for r in range(x1, x2):
        for c in range(y1, y2):
            arr[r][c] += 1

# Rectangle M
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

# 격자로 옮겨야 하니까, (x1,y1) (x2-1, y2-1)
for r in range(x1, x2):
    for c in range(y1, y2):
        arr[r][c] -= 1

# count
totalArea = 0
for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] > 0:
            totalArea += 1

# print
print(totalArea)