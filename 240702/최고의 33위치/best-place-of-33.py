n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

# calculate max coin
def coin(grid, row, end_row, start_col, end_col):
    found = 0
    for r in range(row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if grid[r][c] == 1:
                found += 1
    return found

res = -999
for row in range(n):
    for col in range(n):
        if row + 2 < n and col + 2 < n:
            temp = coin(grid, row, row + 2, col, col + 2)
        else:
            continue

        res = max(res, temp)

print(res)