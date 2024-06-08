# input 
n = int(input())
commands = [ 
    tuple(map(str, input().split())) for _ in range(n)
]

# create checklist
offset = 100
checked = [0] * (2 * offset + 1)
start = offset

for x1, x2 in commands:
    x = int(x1)
    direction = x2
    
    if direction == 'L':
        for i in range(start, start - x, -1):
            checked[i] += 1
        start -= x
    elif direction == 'R':
        for i in range(start, start + x):
            checked[i] += 1
        start += x

ctr = 0
for i in checked:
    if i > 1:
        ctr += 1

print(ctr)