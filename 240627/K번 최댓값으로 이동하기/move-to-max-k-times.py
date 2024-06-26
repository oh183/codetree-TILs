from collections import deque
NOT_EXISTS = (-1, -1)

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split())) for _ in range(n)
]

r, c = map(int, input().split())
curr_cell = (r - 1, c - 1)
q = deque()

def in_range(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True

    else: 
        return False

def can_go(target, nx, ny):
    if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny] < target:
        return True
    else:
        return False

visited = [
    [False for _ in range(n)] for _ in range(n)
]

def BFS():
    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    q.append(curr_cell)
    target = grid[curr_x][curr_y]
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(target, nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def need_update(best_pos, new_pos):
    # 바로 도달 가능한 경우
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    return (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y)

def move():
    global curr_cell
    initialize_visited()
    # 도달 가능한 cell 들을 탐색 
    BFS()

    # 우선순위가 높은 위치를 구하기
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            
            # Not reachable 
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    # 이동
    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True

for _ in range(k):
    is_moved = move()

    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x+1, final_y + 1)