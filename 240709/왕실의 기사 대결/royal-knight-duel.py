from collections import deque

# 격자 크기, 기사의 수, 명령의 수
L, N, Q = map(int, input().split())

# 체스판 정보
chessBoard = [list(map(int, input().split())) for _ in range(L)]

# 기사 정보
# 1. r, c, h, w, k
knightCommands = [
    list(map(int, input().split())) for _ in range(N)
]

# 기사 배열
knight = [[0 for _ in range(L)] for _ in range(L)]
gisa = 1
knightHealth, knightLocation, knightDamage, knightStatus = {}, {}, {}, {}
for command in knightCommands:
    r, c, h, w, k = command
    r, c, w, h = r - 1, c - 1, w, h

    # 기사 위치 저장
    # (1) 배열
    for i in range(r, r + h):
        for j in range(c, c + w):
            knight[i][j] = gisa

    # (2) 딕셔너리
    if gisa not in knightCommands:
        knightLocation[gisa] = (r, c, h, w)

    # 기사 체력
    if gisa not in knightHealth:
        knightHealth[gisa] = k

    # 받은 총 데미지
    if gisa not in knightDamage:
        knightDamage[gisa] = 0

    if gisa not in knightStatus:
        knightStatus[gisa] = 1

    # 기사 번호 증가
    gisa += 1


# range checker
def in_range(i, j):
    return 0 <= i < L and 0 <= j < L

# canGo? -> 기사 안에서만 돌아다니고, 주어진 방향으로만 돌아다니기
def canGo(x, y, direction, bfsDirection, currKnightNumber):
    if direction == bfsDirection:
        return in_range(x, y) and knight[x][y] != 0
    else:
        return in_range(x, y) and knight[x][y] != 0 and knight[x][y] == currKnightNumber

# bfs
def bfs(currR, currC, direction):
    visitedKnights = set()
    q = deque([(currR, currC)])
    visited = [[0 for _ in range(L)] for _ in range(L)]
    visited[currR][currC] = 1
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        currKnightNumber = knight[x][y]
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if canGo(nx, ny, direction, i, currKnightNumber) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                visitedKnights.add(knight[nx][ny])
    return list(visitedKnights)

def deleteKnight(target):
    r, c, h, w = knightLocation[target]
    for row in range(r + h):
        for col in range(c + w):
            knight[row][col] = 0


# 왕의 명령
kingCommands = [list(map(int, input().split())) for _ in range(Q)]

# Q 번에 걸쳐서 시뮬레이션 수행
for kingCommand in kingCommands:
    knightName, direction = kingCommand
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # (1) 기사 이동
    currR, currC, height, width = knightLocation[knightName]
    if currR == -999:
        continue
    next_row, next_col = currR + dxs[direction], currC + dys[direction]

    # 현재 도형에서 1칸만큼 밀었을때 방문 가능했던 배열들
    visitedKnights = bfs(currR, currC, direction)

    isObstacle = 0
    for knight in visitedKnights:
        r, c, h, w = knightLocation[knight]
        if r != -999:
            newRow, newCol = r + dxs[direction], c + dys[direction]
            for i in range(newRow, newRow + h):
                for j in range(newCol, newCol + w):
                    if not in_range(i, j) or chessBoard[i][j] == 2:
                        isObstacle = 1

    # 밀렸던 칸에 벽이 없었던 경우
    if not isObstacle:
        # 업데이트
        for knight in visitedKnights:
            r, c, h, w = knightLocation[knight]
            if r != -999:
                newRow, newCol = r + dxs[direction], c + dys[direction]
                knightLocation[knight] = newRow, newCol, h, w


    # 업데이트 된 배열을 바탕으로 기사배열 초기화
    knight = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(1, N + 1):
        r, c, h, w = knightLocation[i]
        if r != -999:
            for j in range(r, r + h):
                for k in range(c, c + w):
                    knight[j][k] = i

    # (2) 이동 후 대결 데미지 업데이트
    # 업데이트 된 Knight 배열을 순회하며 체력 업데이트
    if not isObstacle:
        for i in range(L):
            for j in range(L):
                currKnight = knight[i][j]
                if currKnight in visitedKnights:
                    if currKnight > 0:
                        if chessBoard[i][j] == 1 and currKnight != knightName:
                            knightHealth[currKnight] -= 1
                            knightDamage[currKnight] += 1

                        if knightHealth[currKnight] == 0:
                            # 말이 죽은 경우
                            deleteKnight(currKnight)
                            knightLocation[currKnight] = (-999, -999, -999, -999)


# 최종 결과 프린트
res = 0
for i in range(1, N + 1):
    if knightHealth[i] > 0 and knightStatus[i] > 0:
        res += knightDamage[i]
print(res)