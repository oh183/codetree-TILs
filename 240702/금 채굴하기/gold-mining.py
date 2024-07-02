n, m = map(int, input().split())
gold_grid = [
    list(map(int, input().split())) for _ in range(n)
]

# 마름모 저장 어레이
marum = [
    [0 for _ in range(n)] for _ in range(n)
]

visited = [
    [0 for _ in range(n)] for _ in range(n)
]

# 시작 k, reward 값
k = -1
curr_reward = -99999

# array scan (find if expansion is not needed)
def outerScan():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if marum[i][j] == 1:
                cnt += 1

    if cnt == (n * n):
        return False
    else:
        return True

# array scan (inner Scan)
def innerScan():
    totalGold = 0
    for i in range(n):
        for j in range(n):
            if marum[i][j] == 1 and gold_grid[i][j] == 1:
                totalGold += 1
    return totalGold

# calculate the cost
def calcReward(k, m):
    gold = innerScan()
    cost = (k * k) + ((k + 1) * (k + 1))
    if (gold * m) - cost >= 0:
        return gold
    else:
        return 0

# range check
dxs, dys = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]
def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

# expand the marummo
def expand(row, col, k):
    global visited, marum
    visited = [
        [0 for _ in range(n)] for _ in range(n)
    ]

    if k == -1:
        # mark the current Cell
        marum[row][col] = 1
    else:
        coords = []
        for i in range(n):
            for j in range(n):
                if marum[i][j] == 1:
                    coords.append((i,j))
                    visited[i][j] = 1
        for x, y in coords:
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny]:
                    marum[nx][ny] = 1
                    visited[nx][ny] = 1
    return k + 1

# traverse the 2d Array
for i in range(n):
    for j in range(n):
        while outerScan():
            k = expand(i, j, k)
            curr_reward = max(calcReward(k, m), curr_reward)
        # reset
        k = -1
        marum = [[0 for _ in range(n)] for _ in range(n)]
print(curr_reward)