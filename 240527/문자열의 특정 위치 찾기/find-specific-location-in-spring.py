string, char = map(str, input().split())

if string.find(char) == -1:
    print("No")
else:
    print(string.find(char))