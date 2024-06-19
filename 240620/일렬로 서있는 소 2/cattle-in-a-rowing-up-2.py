n = int(input())
cows = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if cows[i] <= cows[j] <= cows[k]:
                result += 1

print(result)