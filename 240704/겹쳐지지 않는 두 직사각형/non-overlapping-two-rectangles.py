# 겹쳐지지 않는 두 직사각형
n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

rect_map = [
    [0 for _ in range(m)] for _ in range(n)
]

# clear 하기
def clear():
    for i in range(n):
        for j in range(m):
            rect_map[i][j] = 0

# 직사각형 그리기
def make_rect(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            rect_map[i][j] += 1

# 겹치는 여부 support
def check():
    for i in range(n):
        for j in range(m):
            if rect_map[i][j] > 1:
                return True
    return False

# 겹치는 여부 보기
def overlap(i1, j1, k1, l1, i2, j2, k2, l2):
    clear()
    make_rect(i1, j1, k1, l1)
    make_rect(i2, j2, k2, l2)
    return check()

"""def calc_score():
    res = 0
    for i in range(n):
        for j in range(m):
            if rect_map[i][j] == 1:
                res += grid[i][j]
    return res
"""
def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])

# 첫번째 직사각형 좌표 만들기
def rect_2(x1, y1, x2, y2):
    score = float("-inf")
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlap(x1, y1, x2, y2, i, j, k, l):
                        score = max(score, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))
                    else:
                        clear()
    return score

def rect_1():
    ans =  float("-inf")
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    ans = max(ans, rect_2(i, j, k, l))
    return ans

MYans = rect_1()
print(MYans)