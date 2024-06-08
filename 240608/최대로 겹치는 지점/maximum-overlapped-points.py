n = int(input())
commands = [
    tuple(map(int,input().split())) for _ in range(n)
]
checked = [0] * 101 

for x1, x2 in commands: 
    for i in range(x1, x2 + 1):
        checked[i] += 1

print(max(checked))