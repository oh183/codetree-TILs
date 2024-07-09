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
knightHealth, knightLocation, knightDamage = {}, {}, {}
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
        knightHealth[gisa] = 0

    # 기사 번호 증가
    gisa += 1

# range checker
def in_range(i,j):
    return 0 <= i < N and 0 <= j < N

# 왕의 명령
kingCommands = [list(map(int, input().split())) for _ in range(Q)]

# Q 번에 걸쳐서 시뮬레이션 수행
for kingCommand in kingCommands:
    knightName, direction = kingCommand
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # (1) 기사 이동
    currR, currC, height, width = knightLocation[knightName]
    next_row, next_col = currR + dxs[direction], currC + dys[direction]

    # 해당 위치에 기사가 있는지 확인 (고치기)
    while True:
        counter, stop = 0, 0
        for i in range(next_row, height + 1):
            for j in range(next_col, width + 1):
                if knight[i][j] > 0:
                    if knight[i][j] == knightName:
                        counter += 1
                    else:
                        # 서로 다른 기사인 경우
                        # 기사 범위 찾기
                        gisaName = knight[i][j]
                        r, c, h, w = knightLocation[knightName]
                        for anotherR in range(r, r + h):
                            for anotherC in range(c, c + w):
                                if chessBoard[anotherR][anotherC] == 2:
                                    stop = 1
                                    break
                                else:
                                    continue
                            


                # 만약 벽이나, 범위를 벗어났다면?
                if chessBoard[i][j] == 2 or not in_range(i,j):
                    stop = 1
                    break

        if stop:
            next_row, next_col = currR, currC
            break

        if counter > 0:
            next_row += dxs[direction]
            next_col += dys[direction]

        else:
            break

    # 계산한 next_row, next_col 사용해서 이동
    for i in range(next_row, currR - 1, -1):
        for j in range(next_col, currC - 1, -1):
            if knight[i - 1][j - 1] == 0:
                continue
            else:
                # find the top left point
                gisa = knight[i-1][j-1]
                r, c, h, w = knightLocation[gisa]
                newR, newC = r + dxs[direction], c + dys[direction]
                knightLocation[gisa] = (newR, newC, h, w)


    # 업데이트 된 배열을 바탕으로 기사배열 초기화
    knight = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(1, N + 1):
        r, c, h, w = knightLocation[i]
        for j in range(r, h + 1):
            for k in range(c, w + 1):
                knight[j][k] = i

    # (2) 이동 후 대결 데미지 업데이트
    # 업데이트 된 Knight 배열을 순회하며 체력 업데이트
    for i in range(L):
        for j in range(L):
            currKnight = knight[i][j]
            if chessBoard[i][j] == 1 and currKnight != knightName:
                knightHealth[currKnight] -= 1
                knightDamage[currKnight] += 1

# 최종 결과 프린트
for i in range(1, N + 1):
    if knightHealth[i] > 0:
        print(knightDamage[i], end = " ")