# get the input
string = str(input())

# define target
targetOne = 'ee'
targetOneCtr = 0

targetTwo = 'eb'
targetTwoCtr = 0

for i in range(len(string) -1):
    if string[i:i+2] == targetOne:
        targetOneCtr += 1
    if string[i:i+2] == targetTwo:
        targetTwoCtr += 1

print(targetOneCtr, targetTwoCtr)