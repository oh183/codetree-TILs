n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

# create a grid (n x n)
grid = [
    [0 for _ in range(n)] for _ in range(n)
]

# r, c is an initial position
x, y = r, c

# d is an initial direction
direction = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

curr_dir = direction[d]
dirr = curr_dir

# range checker
def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

# define dx dy 
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

# simulation begins
while t > 0:
    nx, ny = x + dxs[dirr], y + dys[dirr]

    if not in_range(nx, ny, n):
        dirr = 3 - dirr
        t -= 1
        continue
    
    # move
    x, y = x + dxs[dirr], y + dys[dirr]
    t -= 1 

print(x + 1, y + 1)