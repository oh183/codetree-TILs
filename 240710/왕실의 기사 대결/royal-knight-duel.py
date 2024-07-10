from collections import deque

# Global Variables
MAX_KNIGHT = 31
MAX_CHESS = 41
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

info = [[0 for _ in range(MAX_CHESS)] for _ in range(MAX_CHESS)]
init_health = [0 for _ in range(MAX_KNIGHT)]

row_knight = [0 for _ in range(MAX_KNIGHT)]
col_knight = [0 for _ in range(MAX_KNIGHT)]
height_knight = [0 for _ in range(MAX_KNIGHT)]
width_knight = [0 for _ in range(MAX_KNIGHT)]
health_knight = [0 for _ in range(MAX_KNIGHT)]
nextRow_knight = [0 for _ in range(MAX_KNIGHT)]
nextCol_knight = [0 for _ in range(MAX_KNIGHT)]
damage_knight = [0 for _ in range(MAX_KNIGHT)]
moved = [False for _ in range(MAX_KNIGHT)]

# 움직이기 체크
def try_move(idx, direction):
    # init
    for i in range(1, n + 1):
        moved[i] = False
        damage_knight[i] = False
        nextRow_knight[i] = row_knight[i]
        nextCol_knight[i] = col_knight[i]

    # bfs
    q = deque([idx])
    moved[idx] = True

    while q:
        x = q.popleft()

        # new direction
        nextRow_knight[x] += dx[direction]
        nextCol_knight[x] += dy[direction]

        # range check
        # 가려고 하는 방향이 1. 격자밖으로 이동히려고 하거나 2. 총 길이가 격자 크기를 초과 하는 경우 
        if nextRow_knight[x] < 1 or nextCol_knight[x] < 1 or nextRow_knight[x] + height_knight[x] - 1 > l or nextCol_knight[x] + width_knight[x] - 1 > l:
            return False

        # collision check
        for i in range(nextRow_knight[x], nextRow_knight[x] + height_knight[x]):
            for j in range(nextCol_knight[x], nextCol_knight[x] + width_knight[x]):
                if info[i][j] == 1:
                    damage_knight[x] += 1
                if info[i][j] == 2:
                    return False
            
        # chain-reaction check
        for i in range(1, n + 1):
            if moved[i] or health_knight[i] <= 0:
                continue
            # 세로로 안겹치는 경우 (Row 가 아래로 갈수록 숫자가 커지니까, r > nr + h - 1 이면 i 번째의 직사각형은 x 번째 직사각형의 아래보다 더 아래에서 시작한다는 뜻
            if row_knight[i] > nextRow_knight[x] + height_knight[x] - 1 or nextRow_knight[x] > row_knight[i] + height_knight[i] - 1: 
                continue
            # 가로로 안겹치는 경우 
            if col_knight[i] > nextCol_knight[x] + width_knight[x] - 1 or nextCol_knight[x] > row_knight[i] + width_knight[i] - 1:
                continue
            
            # 여기까지 도달했으면, 겹치는게 있었다는 뜻이니까 -> 큐에 넣어서 계속 체크
            q.append(x)
            moved[x] = True
            
    damage_knight[idx] = 0
    return True


# 움직이기
def movePiece(idx, d):
    if health_knight[idx] <= 0:
        return

    # 움직일수 있는 경우, 각 기사들을 다시 업데이트
    if try_move(idx, d):
        for i in range(1, n + 1):
            row_knight[i] = nextRow_knight[i]
            col_knight[i] = nextCol_knight[i]
            health_knight[i] -= damage_knight[i]


# 입력값 받기
l, n, q = map(int, input().split())
# 1 부터 받으려고
for i in range(1, l + 1):
    info[i][1:] = map(int, input().split())
for i in range(1, n + 1):
    row_knight[i], col_knight[i], height_knight[i], width_knight[i], health_knight[i] = map(int, input().split())
    init_health[i] = health_knight[i]

for _ in range(q):
    idx, d = map(int, input().split())
    movePiece(idx, d)
    
ans = 0
for i in range(1, n + 1):
    if health_knight[i] > 0:
        ans += init_health[i] - health_knight[i]

print(ans)