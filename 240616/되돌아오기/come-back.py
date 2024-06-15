# input
n = int(input())
commands = [
    tuple(map(str, input().split())) for _ in range(n)
]

# dx dy setup (E -> S -> W -> N)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# set offset
offset = 1000
maxrange = (2 * offset) + 1

# create answer array (2000 * 2000)
answer = [ 
    [0 for _ in range(maxrange)] for _ in range(maxrange)
]

# mark starting point as 999
answer[offset][offset] = 999

# create dictionary
dist_dict = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

# traverse N times
time_e = 0
total = 0
x, y = offset, offset
for direction, distance in commands:
    direction = dist_dict[direction]
    distance = int(distance)
    
    while distance > 0:
        nx, ny = x + dx[direction], y + dy[direction]
        
        if answer[nx][ny] != 999:
            answer[nx][ny] = 1
            time_e += 1
        else:
            total = time_e + 1
            break
        distance -= 1
        x, y = nx, ny

if total == 0:
    print("-1")
else:
    print(total)