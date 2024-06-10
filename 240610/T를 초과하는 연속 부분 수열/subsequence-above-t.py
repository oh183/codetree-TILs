n, target = map(int, input().split())
inputs = input().split()

ans, cnt = 0, 0
for i in range(len(inputs)):
    if i >= 1 and (int(inputs[i]) > 3 and int(inputs[i-1]) > 3):
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)
print(ans)