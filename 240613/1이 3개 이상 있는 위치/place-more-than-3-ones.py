# input
rows = int(input())
grid = [
    input().split() for _ in range(rows)
]

# traverse
dxs, dys= [1, 0, -1, 0], [0, -1, 0, 1]

# Range Check function
def is_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False 

# 상/하/좌/우 체크
total = 0
x, y = 0, 0
cnt = 0

for x in range(len(grid)):
    for y in range(len(grid)):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny, rows) and int(grid[nx][ny]) == 1:
                cnt += 1

        if cnt >= 3:
            total += 1
        cnt = 0

print(total)