n = int(input())
arr_n = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if j == 0:
            arr_n[i][j] = i + 1
        else:
            arr_n[i][j] = arr_n[i][j - 1] + n 
        print(arr_n[i][j], end = " ")
    print()