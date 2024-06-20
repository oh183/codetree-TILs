n = int(input())
myString = str(input())

cnt =0 

for i in range(0, n - 2):
    for j in range(i+1, n-1):
        for k in range(j + 1, n):
            if myString[i] + myString[j] + myString[k] == "COW":
                cnt += 1

print(cnt)