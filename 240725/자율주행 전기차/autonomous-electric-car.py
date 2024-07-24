# 자율주행 전기차
from collections import deque
n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
initX, initY = map(lambda x: int(x) - 1, input().split())
passengers = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# 벽을 -1로 바꾸기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            grid[i][j] = -1

# 승객 번호를 입력하면, 승객의 목적지를 알려주는 dict
destinations, p_grid = {}, [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, m+1):
    sx, sy, destX, destY = passengers[i-1]
    p_grid[sx][sy] = i
    if i not in destinations:
        destinations[i] = [destX, destY]



# 목적지를 찾는 bfs
def findMyDestination(x, y):
    q = deque([(x, y)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    currInputs = []
    dxs, dys = [-1, 1, 0, 0], [0,0,-1,1]
    while q:
        nq = deque()
        for ci, cj in q:
            if p_grid[ci][cj] > 0:
                currInputs.append((ci, cj))

            for dx, dy in zip(dxs, dys):
                nx, ny = ci + dx, cj + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    nq.append((nx, ny))
        if len(currInputs) > 0:
            best = sorted(currInputs, key = lambda x: (x[0], x[1]))[0]
            return best
        q = nq
    return -1

# 그 위치로 가는 bfs
def goToLocation(si, sj, ei, ej, battery):
    q = deque()
    usedBattery = 0
    q.append((si, sj, ei, ej, battery, usedBattery))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[si][sj] = 1
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        nq = deque()
        for si, sj, ei, ej, battery, usedBattery in q:
            # 목적지에 도달한 경우 종료!
            if (si, sj) == (ei, ej):
                return battery, usedBattery
            # 중간에 배터리가 0이하가 될 때, 종료
            if battery < 0:
                return -2

            for dx, dy in zip(dxs, dys):
                nx, ny = si + dx, sj + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] >= 0:
                    visited[nx][ny] = 1
                    nq.append((nx, ny, ei, ej, battery - 1, usedBattery + 1))
        q = nq
    # 갈 수 없으면
    return -1

ci, cj, fuel = initX, initY, c
while True:
    # 맵 안에 더이상 남은 승객이 없으면 리턴합니다
    isPassenger = 0
    for i in range(n):
        isPassenger += sum(p_grid[i])

    if isPassenger == 0:
        break
    # 승객을 태우러 갑니다
    # 승객 위치 찾기
    destination = findMyDestination(ci, cj)
    if isinstance(destination, tuple):
        ei, ej = destination
    else:
        fuel = -1
        break
    # 승객에게 가자!
    result = goToLocation(ci, cj, ei, ej, fuel)
    if isinstance(result, tuple):
        # 연료 업데이트
        remainFuel, usedFuel = result
        fuel = remainFuel
        ci, cj = ei, ej
    else:
        fuel = -1
        break


    # 목적지로 가자!
    passengerNum = p_grid[ci][cj]
    ei, ej = destinations[passengerNum]
    p_grid[ci][cj] = 0
    canGo = goToLocation(ci, cj, ei, ej, fuel)

    if isinstance(canGo, tuple):
        # 연료 업데이트
        rfuel, ufuel = canGo
        fuel = rfuel + (2 * ufuel)
        ci, cj = ei, ej
    else:
        fuel = -1
        break

print(fuel)