a, b = input().split()

temp = ""
result = 0

for i in a:
    if ord('0') <= ord(i) <= ord('9'):
        temp += i
    else:
        result += int(temp)
        temp = ""
        break

for i in b:
    if ord('0') <= ord(i) <= ord('9'):
        temp += i
    else:  
        result += int(temp)
        temp = ""
        break

print(result)