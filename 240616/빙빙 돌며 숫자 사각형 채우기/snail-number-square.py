# get input n(row), m(col)
n, m = tuple(map(int, input().split()))

# create answer array
answer = [
    [0 for _ in range(m)] for _ in range(n)
]

# set default value (direction) R -> D -> L -> U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
direciton = 0

# mark first cell as 1 
answer[0][0] = 1

# set range function
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

# traverse the 2D grid
total_iter = (n * m) + 1
for i in range(2, total_iter):
    next_x, next_y = x + dx[direciton], y + dy[direciton]

    if not in_range(next_x, next_y) or answer[next_x][next_y] != 0:
        # change direction (90' degree turn)
        direciton = (direciton + 1) % 4
    
    # move
    x, y = x + dx[direciton], y + dy[direciton]
    answer[x][y] = i

# print the answer
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = " ")
    print()