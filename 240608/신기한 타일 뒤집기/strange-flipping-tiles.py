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
    black = abs(end - start)
    white = length - black
else:
    black = abs(end - start) + length
    white = 0

print(black, white)