n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# visited 배열
visited = [[0 for _ in range(n)] for _ in range(n)]

# 각 그리드당 계란틀의 상태 표시 0-> 벽이 있다, 1-> 벽이 분리되어 있다
eggWallStatus = {}
for i in range(n):
    for j in range(n):
        if (i, j) not in eggWallStatus:
            eggWallStatus[(i, j)] = [0, 0, 0, 0]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n


from collections import deque


def addEggs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [(i, j)]
    while q:
        x, y = q.popleft()
        brokenWalls = eggWallStatus[(x, y)]
        direction = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visited[nx][ny] == 0 and brokenWalls[direction] == 1:
                q.append((nx, ny))
                visit.append((nx, ny))
                visited[nx][ny] = 1
            direction += 1

    totalEggCells = len(visit)
    # find Sum
    newEggSum = 0
    for x, y in visit:
        newEggSum += grid[x][y]
    newEggVal = newEggSum // totalEggCells

    for x, y in visit:
        grid[x][y] = newEggVal


cnt = 0
while True:
    # 계란틀 분리
    for i in range(n):
        for j in range(n):
            currVal = grid[i][j]
            currDirection = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny):
                    diff = abs(currVal - grid[nx][ny])
                    if l <= diff <= r:
                        currWall = eggWallStatus[(i, j)]
                        currWall[currDirection] = 1
                        eggWallStatus[(i, j)] = currWall
                currDirection += 1

    # 더 이상 이동을 못하는 경우 break (계란틀이 분리가 X)
    isBreak = 0
    for i in range(len(eggWallStatus.keys())):
        isBreak += sum(list(eggWallStatus.values())[i])

    if isBreak == 0:
        break

    # 계란 합치기
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                addEggs(i, j)

    # 벽 초기화
    eggWallStatus = {}
    for i in range(n):
        for j in range(n):
            if (i, j) not in eggWallStatus:
                eggWallStatus[(i, j)] = [0, 0, 0, 0]
    cnt += 1
print(cnt)