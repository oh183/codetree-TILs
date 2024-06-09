# 기본값 설정
offset = 1000
maxRange = 2 * offset
arr = [
    [0 for _ in range(maxRange + 1)] for _ in range(maxRange + 1)
]

# fill in Rectangle 1 and 2 
for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for r in range(x1, x2):
        for c in range(y1, y2):
            arr[r][c] = i + 1

# find min(x1, y1) max(x2, y2)
row, col = [], [] 
for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] == 1:
            row.append(r)
            col.append(c)
x1_min, x2_max, y1_min, y2_max = 0, 0, 0, 0

if row:
    x1_min = min(col)
    y2_max = max(row) + 1

if col:
    y1_min = min(row)
    x2_max = max(col) + 1


# count
print((y2_max - y1_min) * (x2_max - x1_min))