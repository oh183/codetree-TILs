# 시험 감독
n = int(input())
students = list(map(int, input().split()))
headTeacher, subTeacher = map(int, input().split())

# 일단 감독관이 학생들을 감독합니다 (최솟값)

# 무조건 감독관이 1명이 있습니다.
res = 0
for i in range(n):
    students[i] -= headTeacher
    res += 1

# 부감독의 수를 구합니다
for i in range(n):
    if students[i] > 0:
        currVal = students[i] / subTeacher
        if currVal > (students[i] // subTeacher):
            res += (students[i] // subTeacher) + 1
        else:
            res += (students[i] // subTeacher)
print(res)