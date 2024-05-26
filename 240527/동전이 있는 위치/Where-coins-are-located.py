# get n, m
n, m = map(int, input().split())

# create 2d array init with 0's
myarray = [ 
    [0 for _ in range(n)]
    for _ in range(n)
]

# get the rest input
for _ in range(m):
    row, col = map(int, input().split())
    myarray[row - 1][col - 1] = 1

# print
for i in range(n):
    for j in range(n):
        print(myarray[i][j], end = " ")
    print()