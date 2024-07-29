n, m, k = map(int, input().split())
# 마지막에 추가되는 양분의 양
grid = [list(map(int, input().split())) for _ in range(n)]

# 바이러스
virus = [list(map(int, input().split())) for _ in range(m)]
virusGrid = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, age = virus[i]
    virus[i] = r - 1, c - 1, age
    virusGrid[r - 1][c - 1].append(age)  # 바이러스 번호, 나이

# 초기에 각 칸에 5만큼의 양분이 들어있습니다.
yang = [[5 for _ in range(n)] for _ in range(n)]

# K 사이클 동안 반복
for cycle in range(k):
    deadVirus = []
    # 각 바이러스의 양분섭취
    for i in range(n):
        for j in range(n):
            virusFriends = virusGrid[i][j]
            virusFriends.sort()
            lstToPop = []
            for youngVirus in range(len(virusFriends)):
                virusAge = virusFriends[youngVirus]

                if yang[i][j] < virusAge:
                    # 본인 나이만큼 바이러스 섭취 X -> 사망
                    lstToPop.append(youngVirus)
                    deadVirus.append((virusAge, i, j))
                else:
                    # 양분섭취
                    yang[i][j] -= virusAge
                    virusGrid[i][j][youngVirus] += 1

            if lstToPop:
                for p in range(len(lstToPop) - 1, -1, -1):
                    virusAge = virusGrid[i][j][lstToPop[p]]
                    virusGrid[i][j].pop(lstToPop[p])
                    # 바이러스가 죽은 경우 양분으로 전환
                    yang[i][j] += (virusAge // 2)

    # 바이러스 번식
    for i in range(n):
        for j in range(n):
            if len(virusGrid) == 0:
                continue

            existingVirus = virusGrid[i][j]
            for currVirus in existingVirus:
                age = currVirus
                if age % 5 == 0:
                    # 인접한 8칸에 나이가 1인 바이러스가 생깁니다.
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            virusGrid[nx][ny].append(1)

    # 마지막에 양분 추가
    for i in range(n):
        for j in range(n):
            yang[i][j] += grid[i][j]

# k 사이클 이후 살아있는 바이러스의 양 출력
alive = 0
for i in range(n):
    for j in range(n):
        alive += len(virusGrid[i][j])

print(alive)