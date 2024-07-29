N, M, K = map(int, input().split())
add_arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[5]*N for _ in range(N)]     # 초기양분 모두 5

v = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):                  # M개의 나무
    i,j,age = map(int, input().split())
    v[i-1][j-1].append(age)         # 좌표에 나무 추가

for _ in range(K):  # K년 반복 처리
    # [1] 봄+여름: 나이순으로 처리 => 양분부족시 나무 죽고 ==> //2 양분추가
    for i in range(N):
        for j in range(N):
            v[i][j].sort()                  # 어린순으로 처리위해 정렬
            for k in range(len(v[i][j])):   # 순서대로 처리
                if v[i][j][k]<=arr[i][j]:   # 나이보다 양분이 많다면..
                    arr[i][j]-=v[i][j][k]   # 양분흡수
                    v[i][j][k]+=1           # 나이 한살 먹기
                else:                       # 양분없는경우 => 이후나무들은 모두 양분행
                    while k<len(v[i][j]):   # 나머지 나무는 양분!
                        arr[i][j]+=(v[i][j].pop()//2)
                    break

    # [2] 가을: 나이가 5의 배수인경우 인접8칸에 나무 1짜리 생성
    for i in range(N):
        for j in range(N):
            for k in range(len(v[i][j])):   # 현 위치의 모든 나무처리
                if v[i][j][k]%5==0:         # 5의 배수인경우
                    for di,dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
                        ni, nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj].append(1)

    # [3] 겨울: 초기양분만큼 추가
    for i in range(N):
        for j in range(N):
            arr[i][j]+=add_arr[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans+=len(v[i][j])
print(ans)