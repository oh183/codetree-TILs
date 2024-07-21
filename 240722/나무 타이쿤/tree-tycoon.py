# 나무 타이쿤

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
moveRule = [map(int, input().split()) for _ in range(m)]
fertilizer = [[0 for _ in range(n)] for _ in range(n)]

# 좌하단에 비료 초기화
fertilizer[n - 2][0], fertilizer[n - 2][1], fertilizer[n - 1][0], fertilizer[n - 1][1] = 1, 1, 1, 1

# 방향 벡터
dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]


for year in range(m):
    moveDirection, moveAmount = moveRule[year]

    # 영양제 이동
    fertz = []
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j] == 1:
                fertilizer[i][j] = 0
                fertz.append((i, j))

    for x, y in fertz:
        newX, newY = (x + (moveAmount * dxs[moveDirection - 1])) % n, (y + (moveAmount * dys[moveDirection - 1])) % n
        fertilizer[newX][newY] = 1

    # 영양제 투입
    growlocs = []
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j] == 1:
                fertilizer[i][j] = 0
                grid[i][j] += 1
                growlocs.append((i, j))

    # 영양제 투입 위치 대각선으로 높이 1 이상인 만큼 커짐
    for x, y in growlocs:
        for dx, dy in ((-1, 1), (-1, -1), (1, -1), (1, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 0:
                grid[x][y] += 1

    # 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상이면 영양제 + 영양제를 기록
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 1 and (i, j) not in growlocs:
                grid[i][j] = max(0, grid[i][j] - 2)
                fertilizer[i][j] = 1

res = 0
for i in range(n):
    for j in range(n):
        res += grid[i][j]
print(res)