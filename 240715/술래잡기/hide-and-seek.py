n, m, h, k = map(int, input().split())
runners = [list(map(int, input().split())) for _ in range(m)]
for i in range(len(runners)):
    x, y, d = runners[i]
    x, y = x - 1, y - 1
    runners[i] = (x, y, d)
tree = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(h)]

treeMap = [[0 for _ in range(n)] for _ in range(n)]
for x, y in tree:
    treeMap[x][y] = 1

runnerMap = [[0 for _ in range(n)] for _ in range(n)]
number = 1
for x, y, d in runners:
    runnerMap[x][y] = number
    number += 1

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
direction = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 달팽이 경로로 순회 할 경로를 찾습니다
x, y = 0, 0
visited = [[False for _ in range(n)] for _ in range(n)]
visited[x][y] = True
path = [(0, 0, 0)]
for i in range(1, n*n):
    nx, ny = x + dx[direction], y + dy[direction]
    flag = 0
    if not in_range(nx, ny) or visited[nx][ny]:
        direction = (direction + 1) % 4
        flag = 1
    x, y = x + dx[direction], y + dy[direction]
    visited[x][y] = True
    if i + 1 == n*n:
        path.append((x, y, 0))
    else:
        path.append((x, y, flag))


score = 0

followPath = path[::-1] + path + path[::-1] + path + path[::-1]
for turn in range(1, k + 1):
    # 술래 좌표
    soolaeX, soolaeY, directionChange = followPath[turn - 1]
    s_direction = 0

    # 도망자가 움직입니다.
    for runnerNum in range(len(runners)):
        runner = runners[runnerNum]

        if (-999, -999, -999) == runner:
            continue

        # 술래와의 거리 찾기
        runnerX, runnerY, runnerDirection = runner
        dist = abs(runnerX - soolaeX) + abs(runnerY - soolaeY)

        # 거리가 3 이하면 움직임
        if dist <= 3:
            nx, ny = runnerX + dx[runnerDirection], runnerY + dy[runnerDirection]
            if in_range(nx, ny):
                # 술래가 없으면 움직임
                if (nx, ny) != (soolaeX, soolaeY):
                    temp = runnerMap[runnerX][runnerY] - 1
                    runnerMap[runnerX][runnerY] = 0
                    runnerMap[nx][ny] = temp
                    runners[runnerNum] = (nx, ny, runnerDirection)
            else:
                runnerDirection = (runnerDirection + 2) % 4
                nx, ny = runnerX + dx[runnerDirection], runnerY + dy[runnerDirection]
                if (nx, ny) != (soolaeX, soolaeY):
                    temp = runnerMap[runnerX][runnerY] - 1
                    runnerMap[runnerX][runnerY] = 0
                    runnerMap[nx][ny] = temp
                    runners[runnerNum] = (nx, ny, runnerDirection)

    # 술래가 움직입니다.
    newSoolaeX, newSoolaeY, directionChange = followPath[turn]
    if directionChange == 1:
        s_direction = (s_direction + 1) % 4
    # 도망자 잡기: 시야는 정확히 3칸
    runnerCnt = 0
    detectedPos = []
    for i in range(3):
        if not in_range(newSoolaeX, newSoolaeY):
            break

        if treeMap[newSoolaeX][newSoolaeY] == 1:
            newSoolaeX, newSoolaeY = newSoolaeX + dx[s_direction], newSoolaeY + dy[s_direction]
            continue

        if runnerMap[newSoolaeX][newSoolaeY] > 0:
            temp = runnerMap[newSoolaeX][newSoolaeY] - 1
            runnerMap[newSoolaeX][newSoolaeY] = 0
            runners[temp] = (-999, -999, -999)
            runnerCnt += 1

        newSoolaeX, newSoolaeY = newSoolaeX + dx[s_direction], newSoolaeY + dy[s_direction]

    score += turn * runnerCnt





print(score)