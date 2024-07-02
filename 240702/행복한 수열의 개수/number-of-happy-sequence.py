n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

def is_happy(seq, m):
    cnt = 1
    res = 1
    
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        res = max(1, cnt)
    return res >= m

total = 0 
for row in range(n):
    total += is_happy(grid[row][:], m)


vertical = []
val = ""
for col in range(n):
    for row in range(n):
        val += str(grid[row][col])
    vertical.append(val)
    val = ""

for i in vertical:
    total += is_happy(i, m)

print(total)