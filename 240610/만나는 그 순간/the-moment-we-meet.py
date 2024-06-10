N, M = map(int, input().split())

# A 부터 시뮬레이션
offset = 1000000
MaxRange = 2 * offset
a_sim = [0] * (MaxRange + 1)
starting = offset

timestamp = 0

for _ in range(N):
    d, t = input().split()
    t = int(t)

    if d == 'L':
        while t > 0:
            a_sim[starting] = timestamp
            timestamp += 1
            t -= 1

            starting -= 1
    else:
        while t > 0:
            a_sim[starting] = timestamp
            timestamp += 1
            t -= 1

            starting += 1

# B 시뮬레이션
b_sim = [0] * (MaxRange + 1)
starting = offset
timestamp = 0

for _ in range(M):
    d, t = input().split()
    t = int(t)

    if d == 'L':
        while t > 0:
            b_sim[starting] = timestamp
            timestamp += 1
            t -= 1
            starting -= 1
    else:
        while t > 0:
            b_sim[starting] = timestamp
            timestamp += 1
            t -= 1
            starting += 1

# compare
result = -1
for i in range(990, len(a_sim)):
    if a_sim[i] == b_sim[i] and a_sim[i] != 0:
        result = a_sim[i]
        break

print(result)