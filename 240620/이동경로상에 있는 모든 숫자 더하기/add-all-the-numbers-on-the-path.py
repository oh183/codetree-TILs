n, t = map(int, input().split())
commands = input()

arr = [
    list(map(int, input().split())) for _ in range(n)
]

# R -> D -> L -> U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# direction, init
x, y = n // 2, n // 2
direction = 3

# in range function
def in_range(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        return False

# traverse t times
total = arr[x][y]
for i in range(t):
    command = commands[i]
    
    if command == "L":
        direction = (direction + 3) % 4
    elif command == "R":
        direction = (direction + 1) % 4
    else:
        nx, ny = x + dx[direction], y + dy[direction]

        if not in_range(nx, ny):
            continue
        x, y = nx, ny
        total += arr[x][y]

print(total)