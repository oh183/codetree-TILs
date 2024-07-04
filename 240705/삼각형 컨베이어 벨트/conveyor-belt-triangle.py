n, t = tuple(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list(map(int, input().split()))

def push():
    global list1, list2, list3
    temp2 = list1[-1]
    temp3 = list2[-1]
    # 1
    for i in range(n - 1, 0, -1):
        list1[i] = list1[i-1]
    list1[0] = list3[-1]

    # 2
    for j in range(n-1, 0, -1):
        list2[j] = list2[j - 1]
    list2[0] = temp2

    #3 
    for k in range(n-1, 0, -1):
        list3[k] = list3[k - 1]
    list3[0] = temp3

for _ in range(t):
    push()

for i in list1:
    print(i, end = " ")
print()

for i in list2:
    print(i, end = " ")
print()

for i in list3:
    print(i, end = " ")
print()