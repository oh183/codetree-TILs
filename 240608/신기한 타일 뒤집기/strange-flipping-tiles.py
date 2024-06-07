n = int(input())

length = 0
start = 0
end = 0
ctr = 0

commands = [
    tuple(input().split()) for _ in range(n)
]

for x, direction in commands:
    if ctr == n-1:
        break
    else: 
        ctr += 1

    if direction == 'R':
        end = start + int(x)
    else:
        end = start - int(x)

    length = abs(end - start)
    start = end

x, direction = commands[-1]

if direction == 'R':
    end = start + int(x)
else:
    end = start - int(x)

if start > end:
    white = abs(end - start)
    black = length - white
else:
    white = abs(end - start) + length
    black = 0

print(white, black)