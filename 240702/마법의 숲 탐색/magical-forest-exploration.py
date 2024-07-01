from collections import deque

MAX_L = 70
R, C, K = 0, 0, 0
dx, dy = [-1, 0, 1, 0], [0 , 1, 0, -1]
grid2d = [
    [0 for _ in range(MAX_L)] for _ in range(MAX_L + 3)
]
exit = [
    [False for _ in range(MAX_L)] for _ in range(MAX_L + 3)
]

answer = 0


# 위에서 내려오니까 3칸 더 할당
def in_range(y, x):
    return 3 <= y < R + 3 and 0 <= x < C

def resetMap():
    for i in range(R + 3):
        for j in range(C):
            grid2d[i][j] = 0
            exit[i][j] = False


def canGo(y, x):
    flag = 0 <= x - 1 and x + 1 < C and y + 1 < R + 3
    flag = flag and (grid2d[y - 1][x - 1] == 0)
    flag = flag and (grid2d[y - 1][x] == 0)
    flag = flag and (grid2d[y - 1][x + 1] == 0)
    flag = flag and (grid2d[y][x - 1] == 0)
    flag = flag and (grid2d[y][x] == 0)
    flag = flag and (grid2d[y][x + 1] == 0)
    flag = flag and (grid2d[y + 1][x] == 0)
    return flag

def bfs(x, y):
    result = x
    q = deque([(x,y)])
    visit = [
        [False] * C for _ in range(R + 3)
    ]
    visit[x][y] = True
    
    while q:
        cur_x, cur_y = q.popleft()
        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
        
            # 갈 수 있는 상황
            if in_range(nx, ny) and not visit[nx][ny] and (grid2d[nx][ny] == grid2d[cur_x][cur_y] or (grid2d[nx][ny] != 0 and exit[cur_x][cur_y])):
                visit[nx][ny] = True
                q.append((nx, ny))
                result = max(result, nx)
    return result






def down(x, y, d, numberId):
    
    if canGo(x + 1, y):
        down(x + 1, y, d, numberId)
    elif canGo(x + 1, y - 1):
        down(x + 1, y - 1, (d + 3) % 4, numberId)
    elif canGo(x + 1, y + 1):
        down(x + 1, y + 1, (d + 1) % 4, numberId)
    else:
        if not in_range(x - 1, y - 1) or not in_range(x + 1, y + 1):
            # reset the map
            resetMap()
        else:
            # 맨 마지막에 도달했으니, 로케이션을 마크 하고
            grid2d[x][y] = numberId
            for k in range(4):
                grid2d[x + dx[k]][y + dy[k]] = numberId
            
            # 출구 기록
            exit[x+dx[d]][y+dy[d]] = True
            global answer
            # 계산 값 누적
            answer += bfs(x, y) - 3 + 1


        


def main():
    global R, C, K
    R, C, K = map(int, input().split())
    for numberId in range(1, K + 1): # 골렘 번호 id
        col, dirr = map(int, input().split()) # 골렘의 출발 x좌표, 방향 d를 입력받습니다
        down(0, col - 1, dirr, numberId)
    print(answer)

if __name__ == "__main__":
    main()