command = str(input())

cnt = 0 
result = 0

for i in range(len(command) - 2):
    if command[i] + command[i + 1] == "((":
        for j in range(i + 2, len(command) - 1):
            if command[j] + command[j + 1] == "))":
                result += 1
print(result)