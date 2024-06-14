# get input
n, m = tuple(map(int, input().split()))

# create 2d result array
result = [ 
    [0 for _ in range(n)] for _ in range(m)
]

# dx dy technique (right  -> down -> left -> up )
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# range checking function
def in_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

# set initial direction (0 > right, 1 down, 2 left, 3 up)
dirr = 0

# set initial position
result[0][0] = 1
x, y = 0, 0

# traverse the 2d array 
counter = 1
total = (n * m) + 1
for i in range(2, total):
    # next move
    nx, ny = x + dxs[dirr], y + dys[dirr]

    # range check
    if not in_range(nx, ny, n, m) or result[nx][ny] > 0:
        # update the direction
        dirr = (dirr + 1) % 4
    
    # move
    x, y = x + dxs[dirr], y + dys[dirr]
    result[x][y] = i
    
# print the result
for r in range(len(result)):
    for c in range(len(result)):
        print(result[r][c], end =" ")
    print()