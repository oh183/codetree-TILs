n = int(input())
visited = [
    [0 for _ in range(n)] for _ in range(n)
]

# Starting point is rightmost part
x, y = n - 1, n - 1

# create dx dy matrix Direction : L -> U -> R -> D
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
direction = 0

# range 
def in_range(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        return False

# traverse
total = n * n
visited[x][y] = total

for i in range(2, total + 1):
    nx, ny = x + dx[direction], y + dy[direction]
    
    if not in_range(nx, ny) or visited[nx][ny] != 0:
        direction = (direction + 1) % 4
    
    x, y = x + dx[direction], y + dy[direction]
    visited[x][y] = total - i + 1

# print
for r in range(n):
    for c in range(n):
        print(visited[r][c], end = " ")
    print()