from collections import deque

n, m = map(int, input().split())
# in range 함수를 안만들기 위해서 1 로 둘러쌈
arr = [[1] * (n + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * (n + 2)]

# Base Camp 위치표시
basecamp = set()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            basecamp.add((i, j))
            arr[i][j] = 0

# 편의점 위치 표시
store = {}
for m in range(1, m + 1):
    row, col = map(int, input().split())
    store[m] = (row, col)


# 최단거리 찾는 bfs
def find(x, y, number):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    visited[x][y] = 1
    arrivedList = []

    while q:
        # 동일 반경 처리 BFS
        nq = deque()
        for ci, cj in q:
            if (ci, cj) in number:
                arrivedList.append((ci, cj))
            else:
                # 방문 시작
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = ci + dx, cj + dy
                    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                        visited[nx][ny] = visited[ci][cj] + 1
                        nq.append((nx, ny))
        if len(arrivedList) > 0:
            arrivedList.sort()
            return arrivedList[0]
        q = nq
    return -1


# 다 찾을때까지 계속하는 bfs
def solve():
    time = 1
    q = deque()
    arrived = [0] * (m + 1)

    while q or time == 1:
        nq = deque()
        noMoreMove = []

        # 1) 각 말당 한칸씩 이동
        for x, y, number in q:
            if arrived[number] == 0:
                newX, newY = find(store[number][0], store[number][1],
                                  set(((x - 1, y), (x + 1, y), (x, y-1), (x, y+1))))
                if (newX, newY) == store[number]:
                    arrived[number] = time
                    noMoreMove.append((newX, newY))
                else:
                    # 말을 계속 이동
                    nq.append((newX, newY, number))
        q = nq

        # 2) 만약에 방문했으면, 이제 방문 못함
        if len(noMoreMove) > 0:
            for nr, nc in noMoreMove:
                arr[nr][nc] = 1

        # 3) time <= m 인 경우에 베이스 캠프로 이동
        if time <= m:
            currX, currY = store[time]
            newX, newY = find(currX, currY, basecamp)
            basecamp.remove((newX, newY))
            # 방문 처리
            arr[newX][newY] = 1
            q.append((newX, newY, time))

        time += 1
    return max(arrived)


ans = solve()
print(ans)