# get input
n = int(input())

# create triangle-shaped 2d array
myarray = [
    [1 for _ in range(col + 1)] for col in range(n)
]

# operation
for i in range(n):
    for j in range(i):
        # condition 1: row > 1, col > 0
        if (i > 1 and j > 0) and (j <= i - 1):
            myarray[i][j] = myarray[i-1][j-1] + myarray[i-1][j]


# print
for i in range(n):
    for j in range(i + 1):
        print(myarray[i][j], end = " ")
    print()