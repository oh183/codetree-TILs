r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

for ans in range(101):  # 100초 이내에 답 찾는 경우 break
    if 0 <= r < len(arr) and 0<= c < len(arr[0]) and arr[r][c] == k:
        break
    
    # 행의 개수가 열의 개수보다 작은 경우
    flag = 0
    if len(arr) < len(arr[0]):
        flag = 1
        # 전치행렬
        arr = list(map(list, zip(*arr)))
    
    for i in range(len(arr)):
        occurence = {}
        for j in range(len(arr[i])):
            if arr[i][j] == 0: 
                continue
            if arr[i][j] not in occurence:
                occurence[arr[i][j]] = 1
            else:
                occurence[arr[i][j]] += 1
        
        # 정렬
        lsts = sorted(occurence.items(), key = lambda x: (x[1], x[0]))

        newArr = []
        for itemz in lsts:
            for element in itemz:
                newArr.append(element)
        arr[i] = newArr

    # 100 개가 넘어가는 경우 
    maxColNum = 0
    for i in range(len(arr)):
        maxColNum = max(maxColNum, len(arr[i]))
    
    for i in range(len(arr)):
        while len(arr[i]) < maxColNum:
            arr[i].append(0)
        
        while len(arr[i]) > maxColNum:
            arr[i].pop()
    
    if flag == 1:
        arr = list(map(list, zip(*arr)))

else:
    ans = -1

print(ans)