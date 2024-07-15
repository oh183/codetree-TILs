# 술래잡기
n, m, h, k = map(int, input().split())

# 도망자 좌표
runner = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    x, y, d = runner[i]
    x, y = x-1, y -1
    runner[i] = [x, y, d]


# 나무 좌표
tree = set()
for i in range(h):
    x, y = map(int, input().split())
    x, y = x-1, y -1
    tree.add((x, y))


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

score = 0

# 달팽이 초기 세팅
centerX, centerY = (((n + 1) // 2) -1), (((n + 1) // 2) -1)
maxCnt, cnt, flag, val = 1, 0, 0, 1
direction = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for turn in range(1, k + 1):
    # [1] 도망자들이 이동합니다
    for i in range(len(runner)):
        runnerX, runnerY, d = runner[i]
        dist = abs(runnerX - centerX) + abs(runnerY - centerY)
        if dist <= 3:
            newX, newY = runnerX + dx[d], runnerY + dy[d]
            if in_range(newX, newY):
                if (newX, newY) != (centerX, centerY):
                    runner[i][0], runner[i][1] = newX, newY
            else:
                d = (d + 2) % 4
                runner[i][2] = d
                newX, newY = runnerX + dx[d], runnerY + dy[d]
                if (newX, newY) != (centerX, centerY):
                    runner[i][0], runner[i][1] = newX, newY

    # [2] 술래가 이동합니다
    cnt += 1
    centerX, centerY = centerX + dx[direction], centerY + dy[direction]

    if (centerX, centerY) == (0, 0):
        maxCnt, cnt, flag, val = n, 1, 1, -1
        direction = 2
    elif (centerX, centerY) == ((((n + 1) // 2) -1), (((n + 1) // 2) -1)):
        maxCnt, cnt, flag, val = 1, 0, 0, 1
        direction = 0
    else:
        if cnt == maxCnt:
            direction = (direction + val) % 4
            cnt = 0

            if flag == 0:
                flag = 1
            else:
                maxCnt += val
                flag = 0

    # [3] 술래가 도망자를 척결합니다
    tset = set(((centerX,centerY),(centerX+dx[direction],centerY+dy[direction]),(centerX+dx[direction]*2,centerY+dy[direction]*2)))
    for i in range(len(runner)-1,-1,-1):
        if (runner[i][0],runner[i][1]) in tset and (runner[i][0],runner[i][1]) not in tree:
            runner.pop(i)
            score += turn

print(score)