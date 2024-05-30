a, b = input().split()

temp = ""
result = 0

for i in a:
    if ord('0') <= ord(i) <= ord('9'):
        temp += i
    else:
        break

result += int(temp)
temp = ""

for i in b:
    if ord('0') <= ord(i) <= ord('9'):
        temp += i
    else:
        break

result += int(temp)

print(result)