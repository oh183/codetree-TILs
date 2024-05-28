# get the first string
string = str(input())
length = len(string)

currStr = list(string)

while length != 1:
    # get the new line of input
    command = int(input())
    
    # execute the command 
    if command > length:
        currStr.pop()
    else:
        currStr.pop(command)

    # print the current string 
    print(''.join(currStr))

    # recalculate the length 
    length = len(currStr)