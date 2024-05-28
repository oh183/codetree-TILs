string, num_commands = map(str, input().split())
num_commands = int(num_commands)

for _ in range(num_commands):
    command = int(input())

    if command == 1:
        string = string[1:] + string[0]
    elif command == 2:
        endpoint = len(string) - 1
        string = string[endpoint] + string[0:endpoint]
    elif command == 3:
        string = string[::-1]
    print(string)