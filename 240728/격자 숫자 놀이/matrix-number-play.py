r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

for ans in range(101):  # 100초 이내에 답 찾는 경우 break
    if 0<=r<len(arr) and 0<=c<len(arr[0]) and arr[r][c]==k:
        break

    # [1] 열연산인경우 전치행렬로 변환해서 처리! => 원상복구
    rmode = 1
    if len(arr)<len(arr[0]):    # 열모드
        rmode = 0
        arr = list(map(list,zip(*arr)))

    # [2] 행단위연산: 숫자와 카운트를 처리 => 정렬
    mxcol = 0
    for i in range(len(arr)):
        cnts = {}
        for j in range(len(arr[i])):
            if arr[i][j]==0:    continue    # 0이라면 카운트하지 않음
            if arr[i][j] in cnts:           # 이미 있는 숫자면 +1
                cnts[arr[i][j]]+=1
            else:                           # 없는 숫자면 1개!
                cnts[arr[i][j]]=1

        lsts = sorted(cnts.items(), key=lambda x:(x[1],x[0]))

        # new = []
        # for lst in lsts:
        #     for n in lst:
        #         new.append(n)
        # arr[i]=new
        arr[i] = [n for lst in lsts for n in lst]
        mxcol = max(mxcol, len(arr[i]))

    # [3] 최대길이(mxcol) 구해서 자르거나 0으로 채우기
    mxcol = min(mxcol, 100)
    for i in range(len(arr)):
        while len(arr[i])<mxcol:    # 0으로 채워야함
            arr[i].append(0)
        while len(arr[i])>mxcol:    # 뒤부터 지워야함
            arr[i].pop()

    if rmode==0:                # 열모드 였다면 원상복구!!
        arr = list(map(list,zip(*arr)))
else:                   # 100초까지 답을 못찾은 경우 -1출력
    ans=-1
print(ans)