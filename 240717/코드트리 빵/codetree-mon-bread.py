from collections import deque

# [Input]
n, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
conv_store = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

baseCamp = set()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            baseCamp.add((i,j))

store = {}
for i in range(1, M+1):
    x,y = conv_store[i - 1]
    store[i] = (x, y)

dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

def find(startX, startY, dests):
    global dxs, dys
    q = deque([(startX, startY)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[startX][startY] = True
    potAns = []
    while q:
        nq = deque()

        for ci, cj in q:
            if (ci, cj) in dests:
                potAns.append((ci, cj))
            else:
                for dx, dy in zip(dxs, dys):
                    nx, ny = ci + dx, cj + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] >= 0:
                        visited[nx][ny] = True
                        nq.append((nx, ny))


        if len(potAns) > 0:
            potAns.sort()
            return potAns[0]

        q = nq
    return -1


def solve():
    q = deque()
    time = 1
    arrived = [0] * (M + 1)
    # [1] 한칸씩 움직어야함
    while q or time == 1:
        nq = deque()
        doNotMove = []
        for ci, cj, m in q:
            if arrived[m] == 0:
                ei, ej = find(store[m][0], store[m][1], set(((ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1))))
                if (ei, ej) == store[m]:
                    doNotMove.append((ei, ej))
                    arrived[m] = time
                else:
                    nq.append((ei, ej, m))
        q = nq

        # [2] 방문처리
        if len(doNotMove) > 0:
            for x, y in doNotMove:
                arr[x][y] = -1


        # [3] 큐에 없는 플레이어들을 베이스캠프로 넣기
        if time <= M:
            si, sj = store[time]
            ei, ej = find(si, sj, baseCamp)
            baseCamp.remove((ei,ej))
            arr[ei][ej] = -1
            q.append((ei, ej, time))

        time += 1
    return max(arrived)

ans = solve()
print(ans)