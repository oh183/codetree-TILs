from collections import deque

n, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    currCtr, currSum = 1, grid[si][sj]
    movedPath = [(si, sj)]
    while q:
        nq = deque()
        for x, y in q:
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and visited[nx][ny] == 0 and L <= abs(grid[nx][ny] - grid[x][y]) <= R:
                    currCtr += 1
                    currSum += 1
                    nq.append((nx, ny))
                    visited[nx][ny] = 1
                    movedPath.append((nx, ny))
        q = nq

    if currCtr > 1:
        for row, col in movedPath:
            grid[row][col] = currSum // currCtr
        return 1
    return -1

ans = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                flag = max(bfs(i, j), flag)

    if flag == 0:
        print(ans)
        break
    else:
        ans += 1