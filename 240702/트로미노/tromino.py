n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# case 1
def case_1():
    result = 0
    for i in range(n):
        for j in range(n - 2):
            cnt = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
            result = max(result, cnt)
    return result

# case 2
def case_2():
    result = 0
    for j in range(n):
        for i in range(n - 2):
            cnt = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
            result = max(result, cnt)
    return result

# case 3
def case_3():
    result = 0
    for i in range(n - 1):
        for j in range(n - 1):
            cnt = grid[i][j] + grid[i + 1][j] + grid[i + 1][j + 1]
            result = max(result, cnt)
    return result

# case 4
def case_4():
    result = 0
    result = 0
    for i in range(n - 1):
        for j in range(n - 1):
            cnt = grid[i][j] + grid[i][j + 1] + grid[i + 1][j]
            result = max(result, cnt)
    return result

# case 5
def case_5():
    result = 0
    for i in range(n - 1):
        for j in range(n - 1):
            cnt = grid[i][j] + grid[i][j + 1] + grid[i + 1][j + 1]
            result = max(result, cnt)
    return result

# case 6
def case_6():
    result = 0
    for i in range(n - 1):
        for j in range(n - 1):
            cnt = grid[i + 1][j] + grid[i][j + 1] + grid[i + 1][j + 1]
            result = max(result, cnt)
    return result

total = max(case_1(),case_2(),case_3(),case_4(),case_5(),case_6())
print(total)