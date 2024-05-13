n, m = list(map(int, input().split()))
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(m)
]

ctr = 1

for i in range(n):
    for j in range(m):
        print(ctr, end = " ")
        ctr += 1
    print()