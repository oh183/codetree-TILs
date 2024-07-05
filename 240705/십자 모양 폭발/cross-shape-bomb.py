# 십자 모양 폭발
n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]


visit = [
    [0 for _ in range(n)] for _ in range(n)
]

# dx, dy
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
x, y = r, c

mp = (grid[x][y] - 1)

direction = 0
visit[x][y] = 1
grid[x][y] = 0
for _ in range(4):
    cnt = 0
    nx, ny = x + dxs[direction], y + dys[direction]
    while in_range(nx, ny) and not visit[nx][ny] and cnt < mp:
        grid[nx][ny] = 0
        nx, ny = nx + dxs[direction], ny + dys[direction]
        cnt += 1
    direction = (direction + 1) % 4

# column-wise traverse
temp = []
for j in range(n):
    for i in range(n - 1, -1, -1):
        if grid[i][j] != 0:
            temp.append(grid[i][j])

    # temp.reverse()
    for i in range(n - 1, -1, -1):
        grid[i][j] = 0

    cnt = 0
    for i in range(n - 1, -1, -1):
        if cnt >= len(temp):
            break
        grid[i][j] = temp[cnt]
        cnt += 1
    temp = []

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()