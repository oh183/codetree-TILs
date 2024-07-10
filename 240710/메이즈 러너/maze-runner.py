# 입력
n, m, k = map(int, input().split())

# 미로: 벽, 빈칸이 표시되어 있음
miro = [list(map(int, input().split())) for _ in range(n)]

# 참가자 배열: 참가자들의 좌표가 표시되어 있음
userCoord = [tuple(map(int, input().split())) for _ in range(m)]

# 출구 좌표
exitCoord = tuple(map(int, input().split()))
x, y = exitCoord
exitCoord = (x-1, y - 1)

# 초기 설정 (100 -> 참가자, 99999 -> 출구)
for x, y in userCoord:
    miro[x-1][y-1] = 100
x, y = exitCoord
miro[x][y] = 99999

# 모든 참가자의 이동 거리
moved = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def printList(myArr):
    for i in range(len(myArr)):
        for j in range(len(myArr)):
            print(myArr[i][j], end = " ")
        print()
    print()

for second in range(k):
    # (1) 이동 시작
    # 동시에 이동하기 위해서 만든 참가자 배열
    syncArr = [[0 for _ in range(n)] for _ in range(n)]

    for userX, userY in userCoord:
        userX, userY = userX - 1, userY - 1
        exitX, exitY = exitCoord

        # 거리들을 저장할 배열
        dist = []

        # 현재 거리를 구합니다.
        currDist = abs(userX - exitX) + abs(userY - exitY)
        tempDist = float('inf')

        # 상 -> 하 -> 좌 -> 우 try
        dxs, dys = [-1 , 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx, ny = userX + dxs[i], userY + dys[i]
            if in_range(nx, ny) and (miro[nx][ny] == 0 or miro[nx][ny] == 99999):
                # 범위 안에 있으면 거리 계산
                tempDist = abs(nx - exitX) + abs(ny - exitY)
                dist.append((tempDist, i, nx, ny))

        # 참가자가 새로운 위치로 움직일지 판단
        if dist:
            posArray = sorted(dist, key = lambda x: (x[0], x[1], x[2], x[3]))
            tempDist, dirr, newX, newY = posArray[0]

        if tempDist < currDist:
            # 현재 이동하는 위치가 출구인 경우
            if (newX, newY) == (exitX, exitY):
                # 탈출
                moved += 1
                miro[userX][userY] = 0
            else:
                # 새로 이동하는 위치가 현재 위치보다 출구에 더 가까우면
                miro[userX][userY] = 0
                syncArr[newX][newY] = 100
                moved += 1

    # K 초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다
    cnt = 0
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 100:
                cnt += 1

    if cnt == 0:
        break

    # 배열 싱크
    for i in range(n):
        for j in range(n):
            if syncArr[i][j] == 100:
                miro[i][j] = 100

    # (2) 미로 회전

    # (2-1) 완전탐색으로 가장 작은 정사각형 찾기
    rotate_arr = []
    for size in range(1, n + 1):
        if not rotate_arr:
            for start_row in range(n - size + 1):
                for start_col in range(n - size + 1):
                    userCnt, exitCnt = 0, 0
                    for row in range(start_row, start_row + size):
                        for col in range(start_col, start_col + size):
                            if miro[row][col] == 100:
                                userCnt += 1
                            if miro[row][col] == 99999:
                                exitCnt += 1
                    if userCnt and exitCnt:
                        # 유저와 exit 을 한개라도 포함하는 조합
                        rotate_arr.append((size, start_row, start_col))
    if second == 2:
        abc = 1

    # 모든 조합을 찾은 후 가장 작은 사이즈를 (사이즈 -> r 좌표 크기 -> c 좌표 순으로 정렬)

    smallest = sorted(rotate_arr, key = lambda x: (x[0], x[1], x[2]))
    size, start_row, start_col = smallest[0]

    # 회전을 위해 현재 배열을 복사 (내구도 -1)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = miro[i][j]
    print("Selected Size: ", size, " Start Row: ", start_row, " Start Col: ", start_col)

    # 90도 회전
    newArr = miro[start_row: start_row + size][start_col: start_col + size]
    printList(newArr)
    newCopy = [[0 for _ in range(len(newArr))] for _ in range(len(newArr))]
    for i in range(len(newArr)):
        for j in range(len(newArr)):
            newCopy[i][j] = newArr[i][j]

    for i in range(len(newArr)):
        for j in range(len(newArr)):
            newArr[j][size - i - 1] = newCopy[i][j]

    printList(newArr)
    printList(miro)

    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if 0 < miro[i][j] < 10:
                miro[i][j] -= 1

            if miro[i][j] == 99999:
                exitCoord = (i, j)

    # 참가자 배열 업데이트
    userCoord = []
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 100:
                userCoord.append((i + 1, j + 1))

    print("######## FINAL #########")
    printList(miro)

# 최종 결과 출력
x, y = exitCoord
print(moved)
print(x, y)