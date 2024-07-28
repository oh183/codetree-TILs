n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

n1, n2, n3, n4, n5, n6 = 1, 2, 3, 4, 5, 6
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

from collections import deque


def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def bfs(si, sj):
    value = grid[si][sj]
    q = deque([(si, sj)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[si][sj] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visited[nx][ny] == 0 and grid[nx][ny] == value:
                q.append((nx, ny))
                visited[nx][ny] = 1
    ctr = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                ctr += 1
    return ctr


x, y = 0, 0
dr = 0
result = 0
for turn in range(m):
    nx, ny = x + dxs[dr], y + dys[dr]
    score = 0
    if not in_range(nx, ny):
        dr = (dr + 2) % 4
        nx, ny = x + dxs[dr], y + dys[dr]

    point = grid[nx][ny]
    score = bfs(nx, ny)
    result += (point * score)

    # 면 바꾸기
    if dr == 0:  # 동쪽
        n1, n3, n4, n6 = n4, n1, n6, n3
    elif dr == 1:  # 남쪽
        n1, n2, n5, n6 = n5, n1, n6, n2
    elif dr == 2:  # 서쪽
        n1, n3, n4, n6 = n3, n6, n1, n4
    elif dr == 3:  # 북쪽
        n1, n2, n5, n6 = n2, n6, n1, n5

    # 방향 전환?
    if n6 > grid[nx][ny]:
        dr = (dr + 1) % 4
    elif n6 < grid[nx][ny]:
        dr = (dr + 3) % 4

    x, y = nx, ny

print(result)