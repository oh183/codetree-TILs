# get input
n = int(input())

# initialize 2d array with 0
myarray = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# define end point
endrow = 0
if n % 2 == 0:
    # even number, (n-1, 0)
    endrow = n - 1

# Start iterating
startrow = n - 1
startcol = n - 1
value = 1
direction = 0  # 0 up, 1 down, -1 left

while startrow != endrow or startcol != 0:
    if direction == 0:
        # go up
        while startrow >= 0:
            myarray[startrow][startcol] = value
            value += 1
            startrow -= 1
        startrow = 0
        direction = -1
    elif direction == -1:
        # go left
        startcol -= 1
        myarray[startrow][startcol] = value
        value += 1
        if startrow == n - 1:
            direction = 0
            startrow -= 1
        else:
            direction = 1
            startrow += 1
    elif direction == 1:
        # go down
        while startrow < n:
            myarray[startrow][startcol] = value
            value += 1
            startrow += 1
        direction = -1
        startrow = n-1

for i in range(n):
    for j in range(n):
        print(myarray[i][j], end=" ")
    print()