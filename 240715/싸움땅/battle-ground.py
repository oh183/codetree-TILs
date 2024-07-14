# i love you
# -stephanie-

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 플레이어 정보
player = []
for _ in range(m):
    x, y, d, s = map(int, input().split())
    x, y = x -1, y - 1
    player.append((x, y, d, s))

# 스코어, 총 능력치 저장하는 어레이
scoreBoard, gun = {}, {}
for i in range(m):
    if i not in scoreBoard:
        scoreBoard[i] = 0
        gun[i] = 0

# 플레이어 업데이트
offset = 0
playerArr = [[0 for _ in range(n)] for _ in range(n)]
for playerInfo in player:
    x, y, d, s = playerInfo
    playerArr[x][y] = offset
    offset += 1


# range checker
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def movePlayer(playerNum, x, y, d, s, dx, dy):
    # 이동 후 플레이어의 여부에 따라 2가지 경우
    # 플레이어가 있는 경우
    if playerArr[x][y] > 0:
        # 상대방의 능력
        oppNumber = playerArr[x][y]
        oppX, oppY, oppD, oppS = player[oppNumber]
        oppPower = gun[oppNumber] + oppS

        # 나의 능력
        myPower = gun[playerNum] + s

        # 능력치 비교
        if myPower > oppPower:
            # 내 능력치가 더 큰 경우

            # 이긴 플레이어
            difference = myPower - oppPower
            scoreBoard[playerNum] += difference
            playerArr[x][y] = playerNum
            player[playerNum] = (x, y, d, s)

            # 진 플레이어
            # 해당 셀에 총을 내려놓고, 내 총을 버렸다 처리
            arr[x][y] = max(arr[x][y], gun[oppNumber])
            gun[oppNumber] = 0

            # 다음 방향으로 이동
            nx, ny = x + dx[d], y + dy[d]

            # 방향 찾아주기
            while not in_range(nx, ny) or arr[nx][ny] - 100001 >= 0:
                d = (d + 1) % 4

            # 이동
            nx, ny = nx + dx[d], y + dy[d]

            # 총이 있는지 확인
            if arr[nx][ny] > 0:
                # 총이 있습니다
                gun[oppNumber] = arr[nx][ny]

            playerArr[nx][ny] = oppNumber
            player[playerNum] = (nx, ny, d, s)

        else:
            # 상대방의 능력치가 더 큰 경우
            difference = oppPower - myPower
            scoreBoard[oppNumber] += difference

            # 해당 셀에 총을 내려놓고, 내 총을 버렸다 처리
            arr[x][y] = max(arr[x][y], gun[playerNum])
            gun[playerNum] = 0

            # 다음 방향으로 이동
            nx, ny = x + dx[d], y + dy[d]

            # 방향 찾아주기
            while not in_range(nx, ny) or arr[nx][ny] - 100001 >= 0:
                d = (d + 1) % 4

            # 이동
            nx, ny = nx + dx[d], y + dy[d]

            # 총이 있는지 확인
            if arr[nx][ny] > 0:
                # 총이 있습니다
                gun[playerNum] = arr[nx][ny]

            arr[nx][ny] = 100001 + playerNum
            player[playerNum] = (nx, ny, d, s)

    else:
        # 플레이어가 없는 경우
        currentGun = gun[playerNum]
        newGun = arr[x][y]

        if currentGun < newGun:
            arr[x][y] = currentGun
            gun[playerNum] = newGun

        # 플레이어 이동
        arr[x][y] = 100001 + playerNum
        player[playerNum] = (x, y, d, s)



for round in range(1, k+1):
    # 총 k 턴 만큼 반복하면서 시뮬레이션

    for playerNumber in range(m):
    # 각 플레이어가 본인의 방향대로 1 칸 이동
        x, y, d, s = player[playerNumber]
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        nx, ny = x + dx[d], y + dy[d]

        if in_range(nx, ny):
        # 격자를 벗어나지 않는 경우
            playerArr[x][y] = 0
            movePlayer(playerNumber, nx, ny, d, s, dx, dy)
        else:
        # 격자를 벗어나는 경우 -> 방향이 정 반대로 바뀜 (direction = (direction + 2) % 4, player 배열에도 업데이트
            playerArr[x][y] = 0
            d = (d + 2) % 4
            # 방향 바꾼거 업데이트 해주고
            nx, ny = x + dx[d], y + dy[d]
            player[playerNumber] = (nx, ny, d, s)
            # 해당 방향으로 이동
            movePlayer(playerNumber, nx, ny, d, s, dx, dy)


print(scoreBoard)