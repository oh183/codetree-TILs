myString = str(input())
mylen = int(input())
result = ""

if mylen > len(myString):
    print(myString[::-1])
else:
    for idx, char in enumerate(reversed(myString)):
        if idx < mylen:
            result += char
        else:
            break
    print(result)