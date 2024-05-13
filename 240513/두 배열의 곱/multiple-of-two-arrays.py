arr_1 = []
arr_2 = []

# array 1
for _ in range(3):
    arr_1.append(list(map(int, input().split())))

# space
blank = input()

# array 2
for _ in range(3):
    arr_2.append(list(map(int, input().split())))

# calculation
for i in range(3):
    for j in range(3):
        val = arr_1[i][j] * arr_2[i][j]
        print(val, end = " ")
    print()