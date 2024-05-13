n, m = list(map(int, input().split()))
arr_1 = [[0 for _ in range(m)] for _ in range(n)]
val = 0

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            if j == 0:
                arr_1[i][j] = i
            else:
                arr_1[i][j] = arr_1[i][j - 2] + (n) * 2
        else:
            arr_1[i][j] = 2 * n - arr_1[i][j - 1] - 1

# print
for i in range(n):
    for j in range(m):
        print(arr_1[i][j], end = " ")
    print()