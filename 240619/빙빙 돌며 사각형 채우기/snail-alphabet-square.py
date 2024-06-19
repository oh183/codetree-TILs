alpha = {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H',
    8 : 'I',
    9 : 'J',
    10 : 'K',
    11 : 'L',
    12 : 'M',
    13 : 'N',
    14 : 'O',
    15 : 'P',
    16 : 'Q',
    17 : 'R',
    18 : 'S',
    19 : 'T',
    20 : 'U',
    21 : 'V',
    22 : 'W',
    23 : 'X',
    24 : 'Y',
    25 : 'Z'
}

n, m = map(int, input().split())

# dx dy -> R -> D -> L -> U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0

# range function
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

# init
x, y = 0, 0 
visited = [
    [0 for _ in range(m)] for _ in range(n)
]

visited[0][0] = 1
total = n * m + 1 

for i in range(2, total):
    nx, ny = x + dx[direction], y + dy[direction]

    if not in_range(nx, ny) or visited[nx][ny] != 0:
        direction = (direction + 1) % 4

    x, y =  x + dx[direction], y + dy[direction]
    visited[x][y] = i

# print
for i in range(n):
    for j in range(m):
        print(alpha[(visited[i][j] - 1) % 26], end = " ")
    print()