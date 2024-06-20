n = int(input())
command = list(map(int, input().split()))


value = -999999999
for i in range(len(command)):
    for j in range(i + 2, len(command)):
        temp = command[i] + command[j]
        value = max(value, temp)

print(value)