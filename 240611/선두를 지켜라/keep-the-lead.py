n, m = map(int, input().split())

### initialization
time_restriction = 1000000
arr_a = [0] * (time_restriction + 1)
arr_b = [0] * (time_restriction + 1)

### count A 
time = 0
currentLocation = 0
for _ in range(n):
    v, t = map(int, input().split())

    while t > 0:
        currentLocation += v
        arr_a[time] = currentLocation
        time += 1
        t -= 1

### count B
time = 0
currentLocation = 0
for _ in range(m):
    v, t = map(int, input().split())

    while t > 0:
        currentLocation += v
        arr_b[time] = currentLocation
        time += 1
        t -= 1

### counting 
### 1 -> A Lead 
### 2 -> B Lead
### 3 -> tie 

totalLead = 0
currentLead = 0
for i in range(len(arr_a)):
    # print("Array A: ", arr_a[i], "Array B: ", arr_b[i])
    if arr_a[i] == 0 or arr_b[i] == 0:
        continue

    if 0 < currentLead < 3:
        if currentLead == 1 and arr_a[i] < arr_b[i]:
            currentLead = 2
            totalLead += 1
        
        if currentLead == 2 and arr_a[i] > arr_b[i]:
            currentLead = 1
            totalLead += 1

    else:
        if arr_a[i] > arr_b[i]:
            currentLead = 1
        elif arr_a[i] < arr_b[i]:
            currentLead = 2
        else:
            currentLead = 3
    
print(totalLead)