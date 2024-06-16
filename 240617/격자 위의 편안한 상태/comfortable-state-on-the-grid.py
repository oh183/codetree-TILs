n, m = tuple(map(int, input().split()))

commands = [
    tuple(map(int, input().split())) for _ in range(m)
]

# create n * m grid
grid = [
    [0 for _ in range(n)] for _ in range(n) 
]

# R -> D -> L -> U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# range check
def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

# comfy check
def is_comfort(r, c):
    r, c = r - 1, c - 1
    counter = 0
    for x, y in zip(dx,dy):
        nr, nc = r + x, c + y
        if in_range(nr,nc) and grid[nr][nc] == 1:  
            counter += 1
    if counter > 2:
        return True
    else:
        return False

for r, c in commands:
    grid[r - 1][c - 1] = 1

    if is_comfort(r,c):
        print(1)
    else:
        print(0)