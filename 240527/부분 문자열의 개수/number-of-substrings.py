string = str(input())
target = str(input())
ctr = 0

for i in range(len(string) - 1):
    if string[i: i+2] == target:
        ctr += 1

print(ctr)