commands = str(input())

# dx dy technique R -> D -> L -> U
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# initial direction
direction = 3
x, y = 0, 0

# traverse 
timer = 0 
answer = 0
for command in commands: 
    if command == 'L':
        # left 90 turn 
        direction = (direction - 3) % 4
    elif command == 'R':
        # right 90 turn
        direction = (direction + 1) % 4
    else:
        # proceed to current direction
        x, y = x + dx[direction], y + dy[direction] 
    timer += 1

    if x == 0 and y == 0:
        answer = timer
        break

if timer:
    print(timer)
else:
    print("-1")