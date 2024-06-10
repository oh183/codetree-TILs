n, target = map(int, input().split())
inputs = input().split()

ans, cnt = 0, 0
for i in range(len(inputs)):
    if i >= 1 and (int(inputs[i]) > target and int(inputs[i-1]) > target):
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

if ans == 1:
    print(0)
else:
    print(ans)