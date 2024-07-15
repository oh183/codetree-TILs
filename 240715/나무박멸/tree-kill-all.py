# n -> 격자 크기
# m -> 박멸이 진행되는 년 수
# k -> 제초제의 확산 범위
# c -> 제초제가 남아 있는 년 수
n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
jecho = []
score = 0

# 동시에 나무 성장
def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def jechojae(year):
    global score
    # 나무가 있는 칸에 제초제를 뿌려봄 (4개의 대각선 방향으로 k칸 만큼 전파되게 됩니다)
    tester = [] # (제초제의 성능, 제초제 뿌린 위치(r,c))
    dxs, dys = [-1, -1, 1, 1], [-1, 1, -1, 1]
    for i in range(n):
        for j in range(n):
            effect = 0
            if arr[i][j] > 0:
                effect += arr[i][j]

                for dx, dy in zip(dxs, dys):
                    for mult in range(1, k + 1):
                        nx, ny = i + (mult * dx), j + (mult * dy)
                        if in_range(nx, ny) and arr[nx][ny] > 0:
                            effect += arr[nx][ny]

                        if not in_range(nx, ny) or arr[nx][ny] < 0:
                            break

                tester.append((effect, i, j))

    # 가장 효과가 좋았던 위치 찾기
    if tester:
        tester.sort(key= lambda x: (-x[0], x[1], x[2]))
        killed, row, col = tester[0]
        score += killed

        # 해당 위치에 제초제 살포
        for i in range(k+1):
            for dx, dy in zip(dxs, dys):
                nx, ny = row + (i * dx), col + (i * dy)
                if in_range(nx, ny) and arr[nx][ny] > 0:
                    arr[nx][ny] = -2

        # 제조체 뿌린 시간 기록
        jecho.append((year + c + 1, row, col))


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for year in range(1, m + 1):
    # 제초제가 사라져야하는지 여부 체크
    if len(jecho) > 0:
        for i in range(len(jecho)):
            yearToWake, row, col = jecho[i]
            if year == yearToWake:
                # 제초제 제거
                for jr in range(k + 1):
                    for dx, dy in zip(dxs, dys):
                        nx, ny = row + (i * dx), col + (i * dy)
                        if in_range(nx, ny) and arr[nx][ny] > 0:
                            arr[nx][ny] = 0

                # 제조제 배열에서 제거
                jecho.remove(jecho[i])

    for i in range(n):
        for j in range(n):
            counter = 0
            if arr[i][j] > 0:
                # 나무가 있는 경우 상 하 좌 우 4방향 탐색
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    # 인접한 4칸중에 격자 범위 내에 있고, 나무가 있는 칸 수
                    if in_range(nx, ny) and arr[nx][ny] > 0:
                        counter += 1

                # 업데이트
                arr[i][j] += counter

    # 나무 번식 진행 (어레이 2개 만들어서, 새로운 어레이에 나무 업데이트하고, 맨 마지막에 다시 original 어레이에 업데이트)
    copiedArr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copiedArr[i][j] = arr[i][j]

    for i in range(n):
        for j in range(n):
            counter, emptyCell = 0, []
            if arr[i][j] > 0:
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    # 벽, 다른나무, 제초제 없어야함
                    if in_range(nx, ny) and arr[nx][ny] == 0:
                        counter += 1
                        emptyCell.append((nx, ny))

                for row, col in emptyCell:
                    copiedArr[row][col] += arr[i][j] // counter

    arr = copiedArr

    # 제초제 뿌리기 (완탐)
    jechojae(year)
print(score)