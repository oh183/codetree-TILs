# 드래곤 커브
n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
grid = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x, y, d, g = curves[i]
    curvePath = [d]

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    for _ in range(g):
        for p in range(len(curvePath) -1, -1, -1):
            curvePath.append((curvePath[p] + 1) % 4)

    for i in curvePath:
        nx, ny = x + dx[i], y + dy[i]
        grid[nx][ny] = 1
        x, y = nx, ny

counter = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i+1][j+1]:
            counter += 1

print(counter)