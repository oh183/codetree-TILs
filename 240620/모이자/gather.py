n = int(input())
numbers = list(map(int, input().split()))
result = []

diff = 0 
for i in range(n):
    currLocation = i
    for idx, val in enumerate(numbers):
        diff += val * abs(idx - currLocation)
    result.append(diff)
    diff = 0

print(min(result))