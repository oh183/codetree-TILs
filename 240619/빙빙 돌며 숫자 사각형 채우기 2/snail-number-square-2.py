n, m = map(int, input().split())

# create array visited array n * m
visited = [
    [0 for _ in range(m)] for _ in range(n)
]

# dx dy D -> R -> U - > L
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# in range function
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

# initialize
x, y = 0, 0
direction = 0 
visited[0][0] = 1

# traverse
total_leng = (n * m) + 1
for i in range(2, total_leng):
    nx, ny = x + dx[direction], y + dy[direction]

    # check if it's in range or visited
    if not in_range(nx,ny) or visited[nx][ny] != 0:
        # change the direction
        direction = (direction + 1) % 4
    
    # make the move 
    x, y = x + dx[direction], y + dy[direction]
    visited[x][y] = i

# print
for row in range(n):
    for col in range(m):
        print(visited[row][col], end = " ")
    print()