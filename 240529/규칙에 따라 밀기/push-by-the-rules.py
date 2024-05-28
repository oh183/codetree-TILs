string = str(input())
commands = str(input())

for command in commands: 
    if command == 'L':
        string = string[1:] + string[0]
    elif command == 'R':
        endpoint = len(string) - 1
        string = string[endpoint] + string[0:endpoint]

print(string)