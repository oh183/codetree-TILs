n, m = list(map(int, input().split()))
arr_1 = []
arr_2 = []
result = []

# input 1
for _ in range(n):
    arr_1.append(list(map(int, input().split())))

# input 2
for _ in range(n):
    arr_2.append(list(map(int, input().split())))

# result array
result = [
    [1 for _ in range(n)]
    for _ in range(m)
]

# calculation
for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            result[i][j] = 0
        print(result[i][j], end= " ")
    print()