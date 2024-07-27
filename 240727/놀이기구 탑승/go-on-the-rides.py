n = int(input())
# n0, n1, n2, n3, n4 -> 학생 번호, 학생이 좋아하는 번호
studentInfo = [list(map(int, input().split())) for _ in range(n * n)]

# 2d grid
grid = [[0 for _ in range(n)] for _ in range(n)]

# 친구 기록하는 dict
likeList = {}
studentNums = []
for i in range(n * n):
    n0, n1, n2, n3, n4 = studentInfo[i]
    if n0 not in likeList:
        likeList[n0] = [n1, n2, n3, n4]
    studentNums.append(n0)

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for student in studentNums:
    # 리스트를 순회하면서 친구수, 빈칸수, row, col 기록
    bestLocs = []
    myFriends = likeList[student]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            x, y = i, j
            friendNum, emptyNum = 0, 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    # 좋아하는 친구가 있는경우 + 1
                    if grid[nx][ny] in myFriends:
                        friendNum += 1
                    # 빈칸인 경우 + 1
                    if grid[nx][ny] == 0:
                        emptyNum += 1
            bestLocs.append((friendNum, emptyNum, x, y))

    # 등장위치 결정
    foundLoc = sorted(bestLocs, key=lambda x: (-x[0], -x[1], x[2], x[3]))[0]
    row, col = foundLoc[2], foundLoc[3]
    grid[row][col] = student

# 스코어 계산
res = 0
for i in range(n):
    for j in range(n):
        currStudentNum = grid[i][j]
        currStudentLikeList = likeList[currStudentNum]
        foundLikeStudents = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny):
                # 인접한 곳에 친구가 있는경우
                if grid[nx][ny] in currStudentLikeList:
                    foundLikeStudents += 1

        # 스코어 계산
        if foundLikeStudents > 0:
            res += (10 ** (foundLikeStudents - 1))
print(res)