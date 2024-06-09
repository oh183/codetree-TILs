# 기본 설정
offset = 100000
MaxRange = 2 * offset
CheckList = [0] * (MaxRange + 1)

# 인풋
n = int(input())
commands = [
    tuple(input().split()) for _ in range(n)
]

# 스타팅 포인트 셋
starting = offset

# 리스트 채우기
for x1, x2 in commands:
    x1 = int(x1)
    
    if x2 == 'L':
        while x1 > 0:
            CheckList[starting] = "White"
            x1 -= 1

            if x1:
                starting -= 1
    else:
        while x1 > 0:
            CheckList[starting] = "Black"
            x1 -= 1

            if x1:
                starting += 1

# 흰, 검 찾기
cnt_b, cnt_w = 0, 0
for i in range(MaxRange + 1):
    if CheckList[i] == "Black":
        cnt_b += 1
    elif CheckList[i] == "White":
        cnt_w += 1

# 프린팅
print(cnt_w, cnt_b)