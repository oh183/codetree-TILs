# 인풋 뭉치
commands = str(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = 3

for command in commands:
    # Counter Clockwise
    if command == "L":
        direction = (direction - 1) % 4
        
    # Clockwise
    elif command == "R":
        direction = (direction + 1) % 4

    else:    
        x += dx[direction] 
        y += dy[direction]


print(x, y)