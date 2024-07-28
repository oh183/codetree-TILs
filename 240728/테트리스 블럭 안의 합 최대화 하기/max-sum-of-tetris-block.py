n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

currMax = -12345

# 1
for i in range(n):
    for j in range(m - 3):
        value = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i][j + 3]
        currMax = max(currMax, value)

# 2
for j in range(m):
    for i in range(n - 3):
        value = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
        currMax = max(currMax, value)

# 3
for i in range(n - 1):
    for j in range(m - 1):
        value = grid[i][j] + grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1]
        currMax = max(currMax, value)

# 4
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 2][j + 1]
        currMax = max(currMax, value)

# 5
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j] + grid[i + 1][j] + grid[i][j + 1] + grid[i][j + 2]
        currMax = max(currMax, value)

# 6
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j] + grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
        currMax = max(currMax, value)

# 7
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i + 1][j] + grid[i+1][j + 1] + grid[i+1][j+ 2] + grid[i][j + 2]
        currMax = max(currMax, value)

# 8
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] + grid[i + 2][j]
        currMax = max(currMax, value)

# 9
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
        currMax = max(currMax, value)

# 10
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i+2][j]
        currMax = max(currMax, value)

# 11
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 2]
        currMax = max(currMax, value)

# 12
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 1][j + 1]
        currMax = max(currMax, value)

# 13
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1]
        currMax = max(currMax, value)

# 14
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
        currMax = max(currMax, value)

# 15
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] + grid[i][j + 1]
        currMax = max(currMax, value)

# 16
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i+2][j + 1]
        currMax = max(currMax, value)

# 17
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j] + grid[i+1][j + 1]
        currMax = max(currMax, value)

# 18
for j in range(m - 1):
    for i in range(n - 2):
        value = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 1][j] + grid[i+2][j]
        currMax = max(currMax, value)

# 19
for i in range(n - 1):
    for j in range(m - 2):
        value = grid[i][j] + grid[i][j + 1] + grid[i + 1][j + 1] + grid[i+1][j + 2]
        currMax = max(currMax, value)

print(currMax)