def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def solve():
    for turnNumber in range(1, 1001):
        # 한칸씩 이동합니다
        for player in range(len(shk)):
            playerNum, ci, cj, d = shk[player]

            # 상하좌우 체크
            for dr in dtbl[playerNum][d]:
                nx, ny = ci + dxs[dr], cj + dys[dr]
                if in_range(nx, ny) and v[nx][ny][0] == -1: # range 안이고 독점상태가 아닌경우
                    shk[player] = [playerNum, nx, ny, dr]
                    break
            else:
                # 없었던 경우, 내 독점계약 칸으로 이동
                for dr in dtbl[playerNum][d]:
                    nx, ny = ci + dxs[dr], cj + dys[dr]
                    if in_range(nx, ny) and v[nx][ny][0] == playerNum:
                        shk[player] = [playerNum, nx, ny, dr]
                        break

        # 각 칸의 냄새 1씩 삭제
        for i in range(n):
            for j in range(n):
                if v[i][j][0] != -1:
                    v[i][j][1] -= 1
                    if v[i][j] == 0:
                        v[i][j] = -1


        # 플레이어 삭제 (가장 작은 플레이어만 남기기)
        i=0
        while i<len(shk):
            sn,si,sj,sd=shk[i]
            # 냄새있고(==빈칸이 아니고), 내냄새 아니면 !=sn
            if v[si][sj][0]!=-1 and v[si][sj][0]!=sn:
                shk.pop(i)
            else:                       # 빈칸에 내가 처음 또는 내냄새 => 새냄새 뿌림
                v[si][sj]=[sn,k]
                i+=1

        # 플레이어가 1만 남으면 리턴
        if len(shk)<=1:                 # 1마리 이하면 종료
            return turnNumber

    else:
        # 1000 턴이 넘어가면 리턴
        return -1

n, m, k = map(int, input().split())
initGrid = [list(map(int, input().split())) for _ in range(n)]
initDirec = list(map(int, input().split()))

v = [[[-1] * 2 for _ in range(n)] for _ in range(n)] # playerNum, 소멸턴
shk = [[0] * 4 for _ in range(m)] # playerNum, i, j, d
dtbl = [[[0] * 4 for _ in range(5)] for _ in range(m)] # 우선순위 배열


# v[][], shk 배열 값 저장해주기
for i in range(n):
    for j in range(n):
        if initGrid[i][j] > 0:
            playerNum = initGrid[i][j] - 1
            v[i][j][0], v[i][j][1] = playerNum, k
            shk[playerNum] = [playerNum, i, j, initDirec[playerNum]]

# dtbl 우선순위 룩업테이블
for playernumber in range(m):
    for j in range(1, 5):
        dtbl[playernumber][j] = list(map(int, input().split()))

# 상, 하, 좌, 우
dxs = [0,-1, 1, 0, 0]
dys = [0, 0, 0,-1, 1]

# 1000턴 시작
ans = solve()
print(ans)