# get inputs
string = str(input())
target = str(input())

startpoint = 0
endpoint = len(target)
currStr = string

# while loop
while endpoint <= len(currStr):
    compareString = currStr[startpoint:endpoint]

    if compareString == target:
        currStr = currStr[0:startpoint] + currStr[endpoint: len(currStr)+1]
        startpoint = 0
        endpoint = len(target)
    else:
        # adjust the position
        startpoint += 1
        endpoint += 1

print(currStr)