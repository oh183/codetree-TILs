# 인풋의 조건을 고려한 오프셋 
offset = 100000

# 스타팅 포인트 셋
starting = offset

# 오프셋을 통해 계산된 최대 값 범위
MaxRange = 2 * offset

# 검정, 흰색이 몇번 나온지를 저장하는 배열
totalCount = [0] * (MaxRange + 1)

# 흰색이 몇번 나온지 계산하는 배열
whiteCount = [0] * (MaxRange + 1)

# 검정이 몇번 나온지 계산하는 배열 
blackCount = [0] * (MaxRange + 1)

# 결과값 저장
blackFin, whiteFin, greyFin = 0, 0, 0

### 인풋
n = int(input())
commands = [
    tuple(input().split()) for _ in range(n)
]

### 계산 
for x1, x2 in commands:
    x1 = int(x1)

    if x2 == 'L':
        while x1 > 0:
            totalCount[starting] = "White"
            whiteCount[starting] += 1
            x1 -= 1
            if x1:
                starting -= 1
    else:
        while x1 > 0:
            totalCount[starting] = "Black"
            blackCount[starting] += 1
            x1 -= 1
            if x1:
                starting += 1


### 카운팅
for i in range(MaxRange + 1):
    if blackCount[i] >= 2 and whiteCount[i] >= 2: 
        greyFin += 1
    # 그렇지 않으면 현재 칠해진 색깔이 곧 타일의 색깔입니다.
    elif totalCount[i] == "White": 
        whiteFin += 1
    elif totalCount[i] == "Black": 
        blackFin += 1

### 출력
print(whiteFin, blackFin, greyFin)