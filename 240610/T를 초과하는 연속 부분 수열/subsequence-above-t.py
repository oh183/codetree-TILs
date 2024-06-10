n, target = map(int, input().split())
inputs = input().split()

ans, cnt = 0, 0
for i in range(len(inputs)):
    # is it greater than the target t? 
    if int(inputs[i]) > target:
        # then compare with i - 1
        cnt += 1
    else:
        cnt = 0
    
    ans = max(ans, cnt)
print(ans)