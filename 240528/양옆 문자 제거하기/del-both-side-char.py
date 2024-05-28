string = str(input())
length = len(string) - 1

firstString = string[0:1]
secondString = string[2:length-1]
thirdString = string[length]

print(firstString+secondString+thirdString)