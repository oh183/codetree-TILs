n = int(input())

grid = [
    list(map(int, input().split())) for _ in range(n)
]

coin = 0
for r in range(n):
    for c in range(0, n - 2, 3):
        value = grid[r][c] + grid[r][c + 1] + grid[r][c+2]
        coin = max(coin, value)
print(coin)