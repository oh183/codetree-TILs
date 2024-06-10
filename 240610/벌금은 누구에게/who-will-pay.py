n, m, k = map(int, input().split())

# n 개의 학생을 나타내는 배열 생성
students = [0] * (n + 1)

# m 번 만큼 for loop 생성하며 계산
result = -1 
for i in range(m):
    penalty = int(input())

    # 학생 배열에 마크 
    students[penalty] += 1

    # 체크
    if students[penalty] == k:
        result = penalty

print(result)