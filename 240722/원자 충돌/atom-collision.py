# 원자 충돌
n, m, k = map(int, input().split())
atoms = [list(map(int, input().split())) for _ in range(m)]

# 원자 정보 기록할 그리드
grid = [[[] for _ in range(n)] for _ in range(n)]

# 초기 위치 기록
for i in range(1, m + 1):
    x, y, mass, speed, direction = atoms[i - 1]
    x, y = x - 1, y - 1
    grid[x][y].append([mass, speed, direction])

# 방향
dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def simulate():
    # 자신의 방향으로 자신의 속력만큼 이동합니다
    tempGrid = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > 0:
                for atomEl in grid[i][j]:
                    # 새 위치로 이동
                    ma, s, d = atomEl
                    nx, ny = (i + (s * dxs[d])) % n, (j + (s * dys[d])) % n
                    tempGrid[nx][ny].append([ma, s, d])

                    # 기존 위치 삭제
                    grid[i][j].remove(atomEl)

    for i in range(n):
        for j in range(n):
            grid[i][j] = tempGrid[i][j]

    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > 1:
                # 칸에 2개 이상의 원자가 있는 경우 합성 발생

                # [1] 질량과 속력을 모두 합한 원자
                newSpeed, newMass, newDirec = 0, 0, []
                for atom in grid[i][j]:
                    newSpeed += atom[1]
                    newMass += atom[0]
                    newDirec.append(atom[2])

                # [2] 질량, 속력 결정
                newMass = newMass // 5
                newSpeed = newSpeed // len(newDirec)

                # [2 - 1] 방향 결정
                strCnt, diaCnt, isDiagonal = 0, 0, 0
                for someDirection in newDirec:
                    if someDirection in (1, 3, 5, 7):
                        strCnt += 1

                    if someDirection in (0, 2, 4, 6):
                        diaCnt += 1

                if strCnt == len(newDirec) or diaCnt == len(newDirec):
                    # 상하좌우
                    isDiagonal = 0
                else:
                    # 대각선
                    isDiagonal = 1

                # [4] 4개의 원자로 나눠서 기록해주기
                diagonalDirection, straightDirection = [1, 3, 5, 7], [0, 2, 4, 6]

                # 그리드 초기화
                grid[i][j] = []
                for count in range(4):
                    if isDiagonal == 0:
                        grid[i][j].append([newMass, newSpeed, straightDirection[count]])

                    if isDiagonal == 1:
                        grid[i][j].append([newMass, newSpeed, diagonalDirection[count]])







for i in range(k):
    simulate()

totalMass = 0
for i in range(n):
    for j in range(n):
        if len(grid[i][j]) > 0:
            for currEl in grid[i][j]:
                totalMass += currEl[0]
print(totalMass)