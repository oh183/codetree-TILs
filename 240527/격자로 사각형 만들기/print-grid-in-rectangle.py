# get n 
n = int(input())

# init 2d array with 1's
myarray = [
    [1 for _ in range(n)]
    for _ in range(n)
]

# calculate
for row in range(n):
    for col in range(n):
        if row > 0 and col > 0:
            myarray[row][col] = myarray[row - 1][col] + myarray[row][col - 1] + myarray[row - 1][col - 1]

# print
for i in range(n):
    for j in range(n):
        print(myarray[i][j], end = " ")
    print()