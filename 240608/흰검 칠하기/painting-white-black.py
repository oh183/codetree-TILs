offset = 100000
maxRange = 2 * offset
checkList = [0] * (maxRange + 1)
starting = offset

# input
n = int(input())
commands = [
    tuple(input().split()) for _ in range(n)
]

# fill in the checklist
for x1, x2 in commands:
    x1 = int(x1)

    if x2 == 'R':
        start = starting
        end = start + x1
        starting += x1
        for i in range(start, end):
            if checkList[i] == 0:
                checkList[i] = 'B'
            elif checkList[i] == 'B':
                continue
            else:
                checkList[i] += 'B'
    else:
        start = starting - x1
        end = starting
        starting -= x1
        for i in range(start, end):
            if checkList[i] == 0:
                checkList[i] = 'W'
            elif checkList[i] == 'W':
                continue
            else:
                checkList[i] += 'W'

blackCnt, whiteCnt, white, black, grey = 0, 0, 0, 0, 0
lastColor = 0

for idx, val in enumerate(checkList):
    i = val
    if i != 0:
        for j in i:
            if j == 'B':
                blackCnt += 1
            else:
                whiteCnt += 1
            lastColor = j

        if blackCnt > 1 and whiteCnt > 1:
            grey += 1
            blackCnt, whiteCnt = 0, 0
            continue
        
        if lastColor == 'B':
            black += 1
        else:
            white += 1
    
    blackCnt, whiteCnt = 0, 0

print(white, black, grey)