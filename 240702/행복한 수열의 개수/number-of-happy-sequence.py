n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

def is_happy(seq):
    cnt, res = 1, 1
    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            cnt += 1
        else:
            cnt = 1

        if cnt == m:
            return True
        res = max(res, cnt)
    return res >= m


total = 0 
for row in range(n):
    total += is_happy(grid[row][:])

vertical = []
val = ""
for col in range(n):
    for row in range(n):
        val += str(grid[row][col])
    if is_happy(list(val)):
        total += 1
    val = ""
        
print(total)