n = int(input())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # dx, dy technique
nx, ny = 0, 0 # indicates current location

for _ in range(n):
    direction, value = map(str, input().split())
    value = int(value)

    if direction == "E":
        nx += value * dx[0] 
        ny += dy[0]
    elif direction == "N":
        nx += dx[1]
        ny += value * dy[1]
    elif direction == "W":
        nx += value * dx[2] 
        ny += dy[2]
    else:
        nx += dx[3] 
        ny += value * dy[3]

print(nx, ny)