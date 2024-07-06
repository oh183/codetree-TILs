# input
n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# move_down 가능한지 보는 함수
def canMove(new_x, start, end):
    if 0 <= new_x < n:
        for i in range(start, end):
            if grid[new_x][i] == 1:
                return False
    else:
        return False
    return True

# move_down execute 함수
def moveDown(r, start, end):
    global grid
    # remove the current rectangle at a given point
    if r > 0:
        for i in range(start, end + 1):
            grid[r - 1][i] = 0
    # move the rectangle
        for i in range(start, end + 1):
            grid[r][i] = 1
    else:
        # move the rectangle
        for i in range(start, end + 1):
            grid[r][i] = 1

# 출력 함수
def printGrid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = " ")
        print()

start, end = k - 1, k + m - 1
new_x = -1
while True:
    if canMove(new_x + 1, start, end - 1):
        moveDown(new_x + 1, start, end - 1)
    else:
        printGrid()
        break
    new_x += 1