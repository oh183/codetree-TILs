def fill_number(array, row, col, val, maxrow, maxcol):
    # Fill the current diagonal
    i, j = row, col
    while i < maxrow and j >= 0:
        array[i][j] = val
        val += 1
        i += 1
        j -= 1

    # Move to the next diagonal
    if col + 1 < maxcol:
        fill_number(array, 0, col + 1, val, maxrow, maxcol)
    elif row + 1 < maxrow:
        fill_number(array, row + 1, col, val, maxrow, maxcol)




# input
n, m  = list(map(int, input().split()))

# 2d Array with 0s
arr2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

fill_number(arr2d, 0, 0, 1, n, m)

for i in range(n):
    for j in range(m):
        print(arr2d[i][j], end = " ")
    print()