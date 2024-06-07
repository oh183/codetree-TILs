n = int(input())
commands = [
    tuple(input().split()) for _ in range(n)
]

checklist = [0] * 200

for x1, x2 in commands:
    start = int(x1) + 1
    end = int(x2) - 1
    while start <= end:
        checklist[start] += 1
        start += 1

result = {}

for el in checklist:
    if el not in result:
        result[el] = 1
    else:
        result[el] += 1

maxkey = 0

for key,val in result.items():
    if maxkey < key and val > 1:
        maxkey = key

print(maxkey)