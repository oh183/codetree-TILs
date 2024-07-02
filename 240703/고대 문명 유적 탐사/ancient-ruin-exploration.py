from collections import deque

k, m = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(5)
]
scribbles = list(map(int, input().split()))

visited = [
    [0 for _ in range(5)] for _ in range(5)
]

coords = []
lastIDX = 0

def tbtRange(cx, cy, nx, ny):
    if 0 <= nx <= cx + 1 and 0 <= ny <= cy + 1:
        return True
    else:
        return False

def in_range2(nx, ny):
    if 0 <= nx < 5 and 0 <= ny < 5:
        return True
    else:
        return False

def rotation(center_x, center_y):
    global grid

    sx, sy = center_x - 1, center_y - 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    direction = 0 
    BaseArr = [grid[sx][sy]]
    for i in range(7):
        nx, ny = sx + dx[direction], sy + dy[direction]
        if not tbtRange(center_x, center_y, nx, ny):
            direction = (direction + 1) % 4

        sx, sy = sx + dx[direction], sy + dy[direction]
        BaseArr.append(grid[sx][sy])
    
    # 회전
    temp0, temp1 = BaseArr.pop(), BaseArr.pop()
    BaseArr.insert(0, temp0)
    BaseArr.insert(0, temp1)

    sx, sy = center_x - 1, center_y - 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
             
    direction = 0 
    grid[sx][sy] = BaseArr[0]
    for i in range(1, 8):
        nx, ny = sx + dx[direction], sy + dy[direction]
        if not tbtRange(center_x, center_y, nx, ny):
            direction = (direction + 1) % 4

        sx, sy = sx + dx[direction], sy + dy[direction]
        grid[sx][sy] = BaseArr[i]

def canGo(x, y, val):
    if grid[x][y] == val and not visited[x][y] and in_range2(x,y):
        return True
    else: 
        return False


def bfs(x,y):
    q = deque([(x, y)])
    visited = [
        [0 for _ in range(5)] for _ in range(5)
    ]
    visited[x][y] = 1
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if canGo(nx, ny, grid[cx][cy]):
                visited[nx][ny] = 1
                q.append((nx, ny))
                coords.append((nx, ny))
                cnt += 1
    if cnt > 2:
        return True
    else:
        coords.clear()
        return False

def fill_arr():
    global coords
    global lastIDX
    global scribbles

    for j in (4, -1, -1):
        for i in (4, -1, -1):
            for corr_X, corr_Y in coords:
                if (i, j) == (corr_X, corr_Y):
                    grid[i][j] = scribbles[lastIDX]
                    lastIDX += 1
                    lastIDX % (len(scribbles) - 1)