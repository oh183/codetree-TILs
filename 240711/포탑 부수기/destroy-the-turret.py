from collections import deque

# 입력
n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# 2D 배열 (마지막 공격한 시점 (N*M))
isAttack = [
    [0 for _ in range(m)] for _ in range(n)
]

# 2D 배열 (이번 턴에 involve 된 Cell 기록 (N*M))
isInvolve = [
    [0 for _ in range(m)] for _ in range(n)
]

back_x = [[0] * m for _ in range(n)]
back_y = [[0] * m for _ in range(n)]

def laserAttack(attacker_r, attacker_c, target_r, target_c):
    q = deque([(attacker_r, attacker_c)])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[attacker_r][attacker_c] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    # back 배열 초기화
    for i in range(n):
        for j in range(m):
            back_x[i][j] = 0
            back_y[i][j] = 0

    while q:
        x, y = q.popleft()
        if (x, y) == (target_r, target_c):
            return True

        for i in range(4):
            nx = (x + dx[i] + n) % n
            ny = (y + dy[i] + m) % m

            if not visited[nx][ny] and grid[nx][ny]:
                back_x[nx][ny] = x
                back_y[nx][ny] = y
                q.append((nx, ny))
                visited[nx][ny] = 1
    return False

def cannonAttack(attacker_r, attacker_c, target_r, target_c):
    global totalCannons
    # 타겟 위치에 한발
    grid[target_r][target_c] -= grid[attacker_r][attacker_c]

    # 주변 8곳에 한발씩
    dxs, dys = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = target_r + dx, target_c + dy
        nx = (nx + n) % n
        ny = (ny + m) % m

        if grid[nx][ny] and (nx, ny) != (target_r, target_c):
            grid[nx][ny] -= grid[attacker_r][attacker_c] // 2
            isInvolve[nx][ny] = 1


for turn_Number in range(1, k + 1):
    # (1) 공격자 선정
    # 격자를 순회하며 가장 작은 포탑을 찾습니다
    cannons = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                cannons.append((grid[i][j], isAttack[i][j], i + j, j))
    cannon = sorted(cannons, key=lambda x: (x[0], -x[1], -x[2], -x[3]))
    temp1, temp2, attacker_r, attacker_c = cannon[0]
    attacker_r, attacker_c = attacker_r - attacker_c, attacker_c

    # 가장 작은 캐논을 찾아서 n + m 업데이트
    grid[attacker_r][attacker_c] += n + m
    # 공격자 기록
    isAttack[attacker_r][attacker_c] = turn_Number
    isInvolve[attacker_r][attacker_c] = 1

    # (2) 공격
    # (2-1) 공격 대상 선정: 자신을 제외한 가장 강한 포탑
    targets = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and (i,j) != (attacker_r, attacker_c):
                targets.append((grid[i][j], isAttack[i][j], i + j, j))
    target = sorted(targets, key=lambda x: (-x[0], x[1], x[2], x[3]))
    temp1, temp2, target_r, target_c = target[0]
    target_r, target_c = target_r - target_c, target_c
    isInvolve[target_r][target_c] = 1

    # (2-2) 레이저 공격 시도
    isLaserPossible = laserAttack(attacker_r, attacker_c, target_r, target_c)

    # 경로 역추적
    if isLaserPossible:
        # 타겟 위치에 있는 포탑 공격
        grid[target_r][target_c] -= grid[attacker_r][attacker_c]

        # 인덱스 계산
        cx, cy = back_x[target_r][target_c], back_y[target_r][target_c]

        while attacker_r != cx or attacker_c != cy:
            grid[cx][cy] -= grid[attacker_r][attacker_c] // 2
            next_x, next_y = back_x[cx][cy], back_y[cx][cy]
            isInvolve[cx][cy] = 1
            cx, cy = next_x, next_y

    else:
        # (2-3) 포탄 공격 시도
        cannonAttack(attacker_r, attacker_c, target_r, target_c)

    # (3) 포탑 정비
    for i in range(n):
        for j in range(n):
            if isInvolve[i][j] == 0 and grid[i][j] > 0:
                grid[i][j] += 1

    isInvolve = [[0 for _ in range(m)] for _ in range(n)]


    # Early Stopping Condition
    totalCannons = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                totalCannons += 1

    if totalCannons <= 1:
        break

    # print()
    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j], end=" ")
    #     print()
    # print()


currMax = float('-inf')
for i in range(n):
    for j in range(m):
        currMax = max(currMax, grid[i][j])
print(currMax)