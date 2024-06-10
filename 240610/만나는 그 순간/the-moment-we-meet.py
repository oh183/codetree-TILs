N, M = map(int, input().split())

### Simulation -> Index = time, value = location

### Simulation A
sim_a = [0] * 1000001
timeStamp = 0
location = 0

for _ in range(N):
    d, t = input().split()
    t = int(t)

    if d == "L":
        while t > 0:
            location -= 1
            sim_a[timeStamp] = location
            timeStamp += 1
            t -= 1
    else:
        while t > 0:
            location += 1
            sim_a[timeStamp] = location
            timeStamp += 1
            t -= 1

### Simulation B
sim_b = [0] * 1000001
timeStamp = 0
location = 0

for _ in range(M):
    d, t = input().split()
    t = int(t)

    if d == "L":
        while t > 0:
            location -= 1
            sim_b[timeStamp] = location
            timeStamp += 1
            t -= 1
    else:
        while t > 0:
            location += 1
            sim_b[timeStamp] = location
            timeStamp += 1
            t -= 1

# counting
result = -1
for i in range(len(sim_a)):
    if sim_a[i] == sim_b[i] and sim_a != 0:
        result = i + 1
        break

print(result)