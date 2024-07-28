from collections import deque

n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    answerList = [(si, sj)]
    sumValue = grid[si][sj]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visited[nx][ny] == 0 and (l <= abs(grid[x][y] - grid[nx][ny]) <= r):
                q.append((nx, ny))
                visited[nx][ny] = 1
                answerList.append((nx, ny))
                sumValue += grid[nx][ny]
    if len(answerList) > 1:
        for x, y in answerList:
            grid[x][y] = sumValue // len(answerList)
        return 1
    return -1
            


cnt = 0
while True:
    # 계란틀 분리 (bfs 로 영역을 지정해주기)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                flag = max(bfs(i, j), flag)
    if flag == 0:
        break
    
    cnt += 1
print(cnt)