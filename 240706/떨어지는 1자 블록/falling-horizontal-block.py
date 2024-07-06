# input
n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]


# canGo
def canGo(nx, n, s, e):
    if 0 <= nx < n:
        for col in range(s, e):
            if grid[nx][col] == 1:
                return False
        return True
    else:
        return False

def printGrid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = " ")
        print()

nx = -1
s, e = k - 1, k + m - 1
while True:
    if canGo(nx + 1, n, s, e):
        nx += 1
    else:
        if nx < 0:
            printGrid()
        else:
            for i in range(s, e):
                grid[nx][i] = 1
            printGrid()
        break