# 나무박멸
n, m, k, c = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
growTemp = [[0 for _ in range(n)] for _ in range(n)]
jecho = [[0 for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

totalKilled = 0

for year in range(1, m + 1):
    # [0] 제초제 작업
    for i in range(n):
        for j in range(n):
            if jecho[i][j] < 0:
                jecho[i][j] += 1

    # [1] 나무의 성장
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            # 나무가 있는 경우
            adj_tree = 0
            if tree[i][j] > 0:
                # 4방향 탐색
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and jecho[nx][ny] == 0 and tree[nx][ny] > 0:
                        adj_tree += 1

            # 나무 수 만큼 원래 배열에 업데이트
            tree[i][j] += adj_tree

    # [2] 나무의 번식
    for i in range(n):
        for j in range(n):
            spreadPath = []
            emptyCell = 0
            if tree[i][j] > 0:
                # 나무가 있는 경우 4 방향을 탐색합니다
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and tree[nx][ny] == 0 and jecho[nx][ny] == 0:
                        emptyCell += 1
                        spreadPath.append((nx, ny))

                if emptyCell > 0:
                    add_tree = tree[i][j] // emptyCell

                    for row, col in spreadPath:
                        growTemp[row][col] += add_tree

    # 나무 번식 업데이트
    for i in range(n):
        for j in range(n):
            tree[i][j] += growTemp[i][j]
    growTemp = [[0 for _ in range(n)] for _ in range(n)]


    # [3] 제초제 뿌리기
    # [3-1] 제초제 뿌릴 위치 완전탐색으로 설정
    ddxs, ddys = [-1, -1, 1, 1], [-1, 1, -1, 1]
    jechoTemp = []
    for i in range(n):
        for j in range(n):
            if tree[i][j] > 0:
                killed = 0
                killed += tree[i][j]
                # 4방향 탐색
                for dx, dy in zip(ddxs, ddys):
                    for step in range(1, k + 1):
                        nx, ny = i + dx * step, j + dy * step
                        if in_range(nx, ny):
                            if tree[nx][ny] > 0:
                                killed += tree[nx][ny]
                            elif tree[nx][ny] <= 0 or jecho[nx][ny] < 0:
                                break
                jechoTemp.append((killed, i, j))

    if jechoTemp:
        currScore, jR, jC = sorted(jechoTemp, key=lambda x: (-x[0], x[1], x[2]))[0]

        # [3-2] 제초제 뿌리고 점수 업데이트
        totalKilled += currScore

        tree[jR][jC] = 0
        jecho[jR][jC] = -(c + 1)
        for dx, dy in zip(ddxs, ddys):
            for step in range(1, k + 1):
                nx, ny = jR + dx * step, jC + dy * step
                if in_range(nx, ny):
                    if tree[nx][ny] > 0:
                        tree[nx][ny] = 0
                        jecho[nx][ny] = -(c + 1)

                    elif tree[nx][ny] <= 0 or jecho[nx][ny] < 0:
                        if tree[nx][ny] < 0:
                            break
                        tree[nx][ny] = 0
                        jecho[nx][ny] = -(c + 1)
                        break



print(totalKilled)