n = int(input())
values = [int(input()) for _ in range(n)]

ans, cnt = 0, 0
for i in range(n):
    if (i >= 1) and (values[i] > 0 and values[i-1] > 0) or (values[i] < 0 and values[i-1] < 0):
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)