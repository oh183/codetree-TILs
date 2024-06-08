offset = 100000
maxRange = 2 * offset
checkList = [0] * (maxRange + 1)
starting = offset
prevStart = starting
prevDirec = ""
prevX1 = 0

# input
n = int(input())
commands = [
    tuple(input().split()) for _ in range(n)
]


# fill in the checklist
for x1, x2 in commands:
    x1 = int(x1)

    if x1 == 1:
        if prevX1 > 1:
            starting -= 1
        if x2 == 'R':
            if checkList[starting] == 0:
                checkList[starting] = 'B'
            else: 
                checkList[starting] += 'B'
        else:
            if checkList[starting] == 0:
                checkList[starting] = 'W'
            else: 
                checkList[starting] += 'W'
        continue

    if x2 == 'R':
        start = starting
        end = start + x1
        prevStart = starting
        starting += x1
        for i in range(start, end):
            if checkList[i] == 0:
                checkList[i] = 'B'
            else:
                checkList[i] += 'B'

    else:
        start = starting - x1
        end = starting
        prevStart = starting
        starting -= x1
        for i in range(start, end):
            if checkList[i] == 0:
                checkList[i] = 'W'
            else:
                checkList[i] += 'W'
    prevX1 = x1

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