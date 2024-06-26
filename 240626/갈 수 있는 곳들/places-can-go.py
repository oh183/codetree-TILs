from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]
commands = [
    tuple(map(int, input().split())) for _ in range(k)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

def in_range(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        return False

def can_go(nx, ny):
    if in_range(nx, ny) and not grid[nx][ny] and not visited[nx][ny]:
        return True
    else:
        return False

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
q = deque()
for command in commands:
    sr, sc = command
    q.append((sr - 1, sc - 1))
    visited[sr - 1][sc - 1] = True
bfs()

result = 0 
for i in range(n):
    for j in range(n):
        if visited[i][j] > 0:
            result += 1
print(result)