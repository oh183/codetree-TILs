n, t = tuple(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
# 밀기 함수 
def push():
    global list1, list2
    # 1 번째 배열 한칸 밀기
    temp = list1[-1]
    for i in range(n - 1, 0, -1):
        list1[i] = list1[i - 1]
    list1[0] = list2[-1]

    # 2 번째 배열 두칸 밀기
    for j in range(n-1, 0, -1):
        list2[j] = list2[j - 1]
    list2[0] = temp

for _ in range(t):
    push()

for i in list1:
    print(i, end= " ")
print()
for i in list2:
    print(i, end= " ")