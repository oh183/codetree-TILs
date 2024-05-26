# get the first line. n,m
n, m = map(int, input().split())

# create n*n 2d array with 0's
myarray = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# calculate
counter = 1 
for i in range(m):
    row, col = map(int, input().split())
    myarray[row-1][col-1] = counter
    counter += 1

# print
for i in range(n):
    for j in range(n):
        print(myarray[i][j], end = " ")
    print()