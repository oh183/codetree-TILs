from collections import deque
# 격자 안에서 단일 객체를 이동
n, r, c = list(map(int, input().split()))
grid = [
    list(map(int, input().split())) for _ in range(n)
]
visit = [
    [0 for _ in range(n)] for _ in range(n)
]
res = []

r, c = r - 1, c - 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def canGo(x, y, ox, oy):
    return 0 <= x < n and 0 <= y < n and not visit[x][y] and grid[ox][oy] < grid[x][y]

def bfs(x,y):
    global grid, res, dxs, dys
    q = deque([(x, y)])
    visit = [
        [False for _ in range(n)] for _ in range(n)
    ]
    res.append(grid[x][y])
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        temp = []
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny, x, y):
                val = grid[nx][ny]
                temp.append((val, nx, ny))
                break

        if not temp:
            break

        val, x, y = temp[0]
        q.append((x, y))
        visit[x][y] = True
        res.append(val)


bfs(r, c)
for i in res:
    print(i, end = " ")