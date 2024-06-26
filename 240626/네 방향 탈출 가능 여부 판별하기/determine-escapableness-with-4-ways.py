from collections import deque

# snake
n, m = map(int, input().split())

# grid 
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# in range
def in_range(nx, ny):
    if 0 <= nx < n and 0 <= ny < m:
        return True
    else:
        return False

# visited
visited = [
    [False for _ in range(m)] for _ in range(n)
]

# can go function
def can_go(x, y):
    return in_range(x,y) and grid[x][y] and not visited[x][y]

def bfs():
    while q:
        x, y = q.popleft()

        # direction
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True

q = deque()

# given starting point
q.append((0,0))
visited[0][0] = True

bfs()

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)