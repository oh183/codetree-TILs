def manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n = int(input())
commands = [
    tuple(map(int, input().split())) for _ in range(n)
]

dist = 99999999999999999
temp = 0

for i in range(1, n-1):
    # we're going to skip i th index
    for j in range(0, i-1):
        x1, y1 = commands[j]
        x2, y2 = commands[j + 1]
        temp += manhattan(x1, x2, y1, y2)
    
    # Overlap
    x1, y1 = commands[i - 1]
    x2, y2 = commands[i + 1]
    temp += manhattan(x1, x2, y1, y2)

    for k in range(i + 1, n - 1):
        x1, y1 = commands[k]
        x2, y2 = commands[k + 1]
        temp += manhattan(x1, x2, y1, y2)
    dist = min(dist, temp)
    temp = 0
print(dist)