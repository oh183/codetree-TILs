# 시공의 돌풍
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
tempGrid = [[0 for _ in range(m)] for _ in range(n)]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

# 청소 시작
# 청소기 위치 찾고
airs = []
for i in range(n):
    for j in range(1):
        if grid[i][j] == -1:
            airs.append((i, j))
upperAir, lowerAir = airs[0], airs[1]

for time in range(t):
    tempGrid = [[0 for _ in range(m)] for _ in range(n)]
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    # 먼지의 확산
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and grid[nx][ny] != -1:
                        tempGrid[nx][ny] += grid[i][j] // 5
                        tempGrid[i][j] -= grid[i][j] // 5
    # 업데이트
    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 0:
                grid[i][j] += tempGrid[i][j]

    # 청소기 path 찾기

    upperPath, upperValue = [], []
    currX, currY = upperAir[0], upperAir[1] + 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[currX][currY] = 1
    upperPath.append((currX, currY))
    upperValue.append(grid[currX][currY])
    direction = 0

    while True:
        if (currX, currY) == upperAir:
            break

        nx, ny = currX + dxs[direction], currY + dys[direction]
        if not in_range(nx, ny) or visited[nx][ny] == 1:
            direction = (direction + 1) % 4

        currX, currY = currX + dxs[direction], currY + dys[direction]
        upperPath.append((currX, currY))
        upperValue.append(grid[currX][currY])
        visited[currX][currY] = 1
    upperPath.pop()
    upperValue.pop()

    # 0 삽입
    upperValue.insert(0,0)
    upperValue.pop()

    for i in range(len(upperPath)):
        x, y = upperPath[i]
        grid[x][y] = upperValue[i]

    lowerPath, lowerValue = [], []
    currX, currY = lowerAir[0], lowerAir[1] + 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[currX][currY] = 1
    lowerPath.append((currX, currY))
    lowerValue.append(grid[currX][currY])
    direction = 0
    Ddxs, Ddys = [0, 1, 0, -1], [1, 0, -1, 0]

    while True:
        if (currX, currY) == lowerAir:
            break

        nx, ny = currX + Ddxs[direction], currY + Ddys[direction]
        if not in_range(nx, ny) or visited[nx][ny] == 1:
            direction = (direction + 1) % 4

        currX, currY = currX + Ddxs[direction], currY + Ddys[direction]
        lowerPath.append((currX, currY))
        lowerValue.append(grid[currX][currY])
        visited[currX][currY] = 1
    lowerPath.pop()
    lowerValue.pop()

    # 0 삽입
    lowerValue.insert(0,0)
    lowerValue.pop()

    for i in range(len(lowerPath)):
        x, y = lowerPath[i]
        grid[x][y] = lowerValue[i]


res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            res += grid[i][j]

print(res)