# 돌아가는 팔각의자
from collections import deque

totalList = [[] for _ in range(4)]
for i in range(4):
    mylist = input()
    for j in range(len(mylist)):
        totalList[i].append(int(mylist[j]))

first_chair = deque(totalList[0])
second_chair = deque(totalList[1])
third_chair = deque(totalList[2])
fourth_chair = deque(totalList[3])
chairs = [first_chair, second_chair, third_chair, fourth_chair]
rotate_num = int(input())
rotateCommand = [list(map(int, input().split())) for _ in range(rotate_num)]

def in_range(n):
    return 0 <= n < 4

for i in range(rotate_num):
    n, d = rotateCommand[i]
    n -= 1

    sa, sb = 2, 6
    rotateArr = [0, 0, 0, 0]

    for i in range(3):
        if i == 0:
            if chairs[i][sa] != chairs[i + 1][sb]:
                rotateArr[i] = d
        elif i == 1 or i == 2:
            if chairs[i][sa] != chairs[i + 1][sb]:
                rotateArr[i] = d
        else:
            if chairs[i][sb] != chairs[i - 1][sa]:
                rotateArr[i] = d

    rotateArr[n] = d

    if in_range(n - 1):
        rotateArr[n - 1] *= -1

    if in_range(n + 1):
        rotateArr[n + 1] *= -1

    if in_range(n - 1):
        if rotateArr[n - 1] == 0:
            for i in range(n):
                rotateArr[i] = 0
    if in_range(n + 1):
        if rotateArr[n + 1] == 0:
            for i in range(i, 4):
                rotateArr[i] = 0

    for idx, rot in enumerate(rotateArr):
        chairs[idx].rotate(rot)

s_arr = [0,0,0,0]
for i in range(4):
    if chairs[i][0] == 1:
        s_arr[i] = 1




print(s_arr[0] + 2 * s_arr[1] + 4 * s_arr[2] + 8 * s_arr[3])