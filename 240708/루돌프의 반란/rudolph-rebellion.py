# 예제 1
# 5 7 4 2 2
# 3 2
# 1 1 3
# 2 3 5
# 3 5 1
# 4 4 4

# 예제 1 정답
# 11 6 2 7
################################

# get inputs
n, m, p, c, d = map(int, input().split())
rud_r, rud_c = map(int, input().split())
santa_locs = [
    tuple(map(int, input().split())) for _ in range(p)
]

# create location map
curr_grid = [[0 for _ in range(n)] for _ in range(n)]
for santa_num, santa_row, santa_col in santa_locs:
    curr_grid[santa_row][santa_col] = santa_num

# Santa scoreBoard (-1: dead, 0: DNE, 1: normal, 2: faint)
scoreBoard = {}
for santa_num, santa_row, santa_col in santa_locs:
    if santa_num not in scoreBoard:
        scoreBoard[santa_num] = 0

# Santa Status
statusBoard = {}
for santa_num, santa_row, santa_col in santa_locs:
    if santa_num not in statusBoard:
        scoreBoard[santa_num] = 1

# 초기 루돌프 위치
rud_r, rud_c = rud_r - 1, rud_c - 1 # 1 index -> 0 index
curr_grid[rud_r][rud_c] = 999

# 거리 구하는 함수
def find_santa():
    global rud_r, rud_c
    distance = []
    for i in range(n):
        for j in range(n):
            if curr_grid[i][j] != 999 and curr_grid[i][j] > 0:
                curr_dist = ((rud_r - i) * (rud_r - i)) + ((rud_c - j) * (rud_c - j))
                distance.append((curr_dist, i, j))
    # sort based on the following priority -> dist, r (descending), c (descending)
    calculated_dist = sorted(distance, key=lambda x: (x[0], -x[1], -x[2]))
    value, sr, sc = calculated_dist[0]
    return (sr, sc)

# range checker
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 상호작용 함수
def mutual(santaNum, direction, land_x, land_y):
    init_santaNum = santaNum
    currentSantaNum = curr_grid[land_x][land_y]
    dxs, dys = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    # 랜딩하는 자리에 산타가 이미 있다고 가정하는 함수임

    while True:
        nx, ny = land_x + dxs[direction], land_y + dys[direction]
        nextSantaNum = curr_grid[nx][ny]
        if in_range(nx, ny) and 0 < curr_grid[nx][ny] < 999:
            # 튕겨나간 산타가 1. 격자 안에 있고, 2. 튕긴 자리에 산타가 있다면
            curr_grid[land_x][land_y] = init_santaNum
            curr_grid[nx][ny] = currentSantaNum
        else:
            






# 돌진하는 함수
def move(toR, toC):
    global rud_r, rud_c, c, scoreBoard, statusBoard
    get_dist = []

    # check 8 locations
    dxs, dys = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    direction = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = rud_r + dx, rud_c + dy
        if in_range(nx, ny):
            dist = ((nx - toR) * (nx - toR)) * ((ny - toC) * (ny - toC))
            get_dist.append((dist, nx, ny, direction))
        direction = (direction + 1) % 8

    # sort based on the following priority -> dist, r (descending), c (descending)
    calculated_dist = sorted(dist, key=lambda x: (x[0], -x[1], -x[2], x[3]))
    value, sr, sc, dirr = calculated_dist[0]
    dirr -= 1 # 8에서 끝나니까

    # move
    curr_grid[rud_r][rud_c] = 0
    rud_r, rud_c = sr, sc

    # 충돌 여부 체크
    if curr_grid[rud_r][rud_c] > 0:
        # c 만큼의 점수를 얻게 됩니다
        scoreBoard[curr_grid[sr][sc]] += c
        # c 만큼 루돌프의 방향으로 밀려나게 됩니다
        santa = curr_grid[sr][sc]
        # 루돌프 이동
        curr_grid[sr][sc] = 999
        # 격자 안으로 밀려난 경우 -> 위치 수정, 격자 밖으로 밀려난 경우 -> 없애버리기
        if in_range(sr + (c * dxs[dirr]), sc + (c * dys[dirr])):
            # 상호작용 조건을 만족하는지 체크
            if 0 < curr_grid[sr + dxs[dirr]][sc + dys[dirr]] < 999:
                # 상호작용 시작 : 이미 루돌프는 [sr][sc] 위치로 이동했고,
                # 그 위치에서 c 만큼 간 곳에서 상호작용을 하는지 봐야함.
                # 이 경우에는 새로운 c 만큼 간 곳의 위치를 넘겨주고 /
                s_r, s_c = sr + (c * dxs[dirr]), sc + (c * dys[dirr])

                # c만큼 움직인 산타의 이름, 방향
                mutual()
            else:
                # 상호작용 조건을 만족하지 않음
                # 산타 이동 후
                curr_grid[sr + (c * dxs[dirr])][sc + (c * dys[dirr])] = santa
                # 루돌프 위치 업데이트
                rud_r, rud_c = sr, sc
        else:
            # 격자 밖으로 움직인 경우
            curr_grid[sr][sc] = 0
            statusBoard[curr_grid[sr][sc]] = -1
    else:
        curr_grid[rud_r][rud_c] = 0
        # 충돌 하지 않은 경우: 루돌프 위치만 이동
        rud_r, rud_c = sr, sc
        curr_grid[rud_r][rud_c] = 999



#