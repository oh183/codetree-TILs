from collections import deque

n, m, q = map(int, input().split())
rotateInfo = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(q)]
############ Input ###############

# deque 로 rotate 해서 관리
from collections import deque

circleBoard = [] * n
for i in range(n):
    circleBoard.append(deque(rotateInfo[i]))

for x, d, k in commands:
    isClockWise = 1

    if d == 0:
        circleBoard[x - 1].rotate(k)
    else:
        circleBoard[x - 1].rotate(-k)

# copy Original Arr
temp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        temp[i][j] = circleBoard[i][j]

# 가로 체크
for boardNum in range(n):
    for j in range(n):
        # 좌로 인접 체크
        leftIdx = (j - 1) % n
        if circleBoard[boardNum][j] == circleBoard[boardNum][leftIdx]:
            temp[boardNum][j], temp[boardNum][leftIdx] = 0, 0

        # 우로 인접 체크
        rightIdx = (j + 1) % n
        if circleBoard[boardNum][j] == circleBoard[boardNum][rightIdx]:
            temp[boardNum][j], temp[boardNum][rightIdx] = 0, 0

# 세로 체크
for j in range(n):
    for i in range(n):
        if i == 0:
            # 위 체크
            upIdx = i + 1
            if circleBoard[i][j] == circleBoard[upIdx][j]:
                temp[i][j], temp[upIdx][j] = 0, 0
        elif 1 <= i < n - 1:
            # 위, 아래 체크
            upIdx, downIdx = i + 1, i - 1

            if circleBoard[i][j] == circleBoard[upIdx][j]:
                temp[i][j], temp[upIdx][j] = 0, 0

            if circleBoard[i][j] == circleBoard[downIdx][j]:
                temp[i][j], temp[downIdx][j] = 0, 0

        else:
            # 아래 체크
            downIdx = i - 1
            if circleBoard[i][j] == circleBoard[downIdx][j]:
                temp[i][j], temp[downIdx][j] = 0, 0

res = 0
for i in range(n):
    res += sum(temp[i])

print(res)