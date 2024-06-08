offset = 1000
maxRange = 2 * offset
checkList = [0] * (maxRange + 1)

# Get input
n = int(input())
commands = [
    tuple(map(str, input().split())) for _ in range(n)
]

# starting Pt
starting = 1000

# Fill the checklist
for x1, x2 in commands:
    x1 = int(x1)

    if x2 == "R":
        # going right
        start = starting
        end = start + x1
        starting += x1
    else:
        # going left
        start = starting - x1 
        end = starting
        starting -= x1 
    
    for i in range(start, end):
        checkList[i] += 1

ctr = 0
for i in checkList:
    if i > 1:
        ctr += 1

print(ctr)