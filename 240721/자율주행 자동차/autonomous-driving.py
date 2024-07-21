from collections import deque

n, m = map(int, input().split())
initX, initY, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

#(N -> E -> S -> W)
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def simulate(startX, startY, direc):
    visited[startX][startY] = 1

    for _ in range(4):
        direc = (direc + 3) % 4
        if in_range(startX + dxs[direc], startY + dys[direc]) and visited[startX + dxs[direc]][startY + dys[direc]] == 0 and grid[startX + dxs[direc]][startY + dys[direc]] == 0:
            visited[startX + dxs[direc]][startY + dys[direc]] = 1
            return startX + dxs[direc], startY + dys[direc], direc, 0


    return startX + dxs[(direc + 2) % 4], startY + dys[(direc + 2) % 4], direc, 1

while True:
    initX, initY, d, flag = simulate(initX, initY, d)
    if flag == 0:
        continue
    else:
        if grid[initX][initY] == 1:
            break

res = 0
for i in range(n):
    res += sum(visited[i])
print(res)