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


def rotate_submatrix(matrix, start_row, start_col, size):
    # 일부분 추출
    submatrix = [row[start_col:start_col + size] for row in matrix[start_row:start_row + size]]

    # Create a new submatrix to store the rotated version
    rotated_submatrix = [[0 for _ in range(size)] for _ in range(size)]

    # 90도 회전
    for i in range(size):
        for j in range(size):
            rotated_submatrix[j][size - 1 - i] = submatrix[i][j]

    # 다시 업데이트
    for i in range(size):
        for j in range(size):
            matrix[start_row + i][start_col + j] = rotated_submatrix[i][j]

    return matrix


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
            else:
                syncArr[userX][userY] = 100
        else:
            syncArr[userX][userY] = 100

    # 배열 싱크
    for i in range(n):
        for j in range(n):
            if syncArr[i][j] == 100:
                miro[i][j] = 100

    # 참가자 배열 업데이트
    userCoord = []
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 100:
                userCoord.append((i + 1, j + 1))
    # (2) 미로 회전

    # (2-1) 완전탐색으로 가장 작은 정사각형 찾기
    rotate_arr = []
    for size in range(2, n + 1):
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

    # 모든 조합을 찾은 후 가장 작은 사이즈를 (사이즈 -> r 좌표 크기 -> c 좌표 순으로 정렬)
    if rotate_arr:
        smallest = sorted(rotate_arr, key=lambda x: (x[0], x[1], x[2]))
        size, start_row, start_col = smallest[0]

        # 회전을 위해 현재 배열을 복사 (내구도 -1)
        miro = rotate_submatrix(miro, start_row, start_col, size)

        # 내구도 업데이트
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

    # K 초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다
    cnt = 0
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 100:
                cnt += 1

    if cnt == 0:
        break

# 최종 결과 출력
x, y = exitCoord
print(moved)
print(x + 1, y + 1)