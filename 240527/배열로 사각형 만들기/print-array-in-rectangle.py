n = 5

myarray = [
    [1 for _ in range(5)]
    for _ in range(5)
]

for i in range(n):
    for j in range(n):
        if i > 0 and j > 0:
            myarray[i][j] = myarray[i-1][j] + myarray[i][j-1]

for i in range(n):
    for j in range(n):
        print(myarray[i][j], end = " ")
    print()