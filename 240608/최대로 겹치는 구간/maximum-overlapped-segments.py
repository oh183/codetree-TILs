n = int(input())
commands = [
    tuple(map(int,input().split())) for _ in range(n)
]

checklist = [0] * 201

for x1, x2 in commands:
    x1, x2 = x1 + 100, x2 + 100

    for i in range(x1, x2):
        checklist[i] += 1

max_num = max(checklist)

print(max_num)