def in_range(x, y):
    return 0 <= x < N and 0 <= y < N
def solve():
    # 1000턴 동안 리턴못하면 -1을 리턴
    for ans in range(1, 1001):  # 4개이상 쌓였으면 ans리턴
        # 말 순서대로 처리
        for i in range(K):
            # [1] 이동위치 계산(ci, cj),(ni, nj), 방향확정!
            ci,cj,dr = lst[i]
            ni,nj=ci+di[dr],cj+dj[dr]
            if not in_range(ni, nj) or arr[ni][nj] == 2:  # 이동할 위치가 파란칸
                dr=opp_dr[dr]   # 반대방향으로..
                ni,nj=ci+di[dr],cj+dj[dr]   # 반대방향 이동할 위치
                lst[i][2]=dr        # 방향 update
                if not in_range(ni, nj) or arr[ni][nj]==2:  # 이동중지! 다음말로..
                    continue

            # [2] 흰색/빨간색에 따라 이동처리(이동위치에 더하고, 지금위치에서 빼고)
            for idx in range(len(v[ci][cj])):
                if v[ci][cj][idx]==i:           # 리스트에서 내번호 찾기
                    mlst=v[ci][cj][idx:]        # 내 말 위에 있는 말들까지 이동후보
                    if arr[ni][nj]==1:          # 빨간칸이면 뒤집어줌(순서)
                        mlst=mlst[::-1]
                    v[ni][nj]+=mlst
                    if len(v[ni][nj])>=4:       # 종료조건 체크
                        return ans

                    v[ci][cj]=v[ci][cj][:idx]   # 현재위치에서 제거
                    for j in mlst:              # 이동시킨 번호 업데이트
                        lst[j][0],lst[j][1]=ni,nj
                    break
    else:                       # 1000턴동안 리턴못함..
        return -1

#        우,좌,하,상
di = [ 0, 0, 0,-1, 1]
dj = [ 0, 1,-1, 0, 0]
opp_dr = {1:2, 2:1, 3:4, 4:3}   # 반대방향 저장

N, K = map(int, input().split())
# 외부와 파란색의 이동이 동일하니 외부를 파란색으로 둘러싸기
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[[] for _ in range(N)] for _ in range(N)]

lst = []
for k in range(K):      # 말 입력(0 ~ K-1)
    i, j, d = list(map(int, input().split()))
    i -= 1
    j -= 1
    lst.append([i, j, d])
    v[i][j].append(k)   # 말 초기위치 v[]에 표시

ans = solve()
print(ans)