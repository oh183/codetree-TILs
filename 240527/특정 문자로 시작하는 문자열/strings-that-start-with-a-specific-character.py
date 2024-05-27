n = int(input())
myArray = [
    input() for _ in range(n)
]

targetChar = str(input())


# Calculate 
totalWord = 0
totalLength = 0

for word in myArray:
    if word[0] == targetChar:
        totalWord += 1
        totalLength += len(word)

# print 
totalAvg = totalLength / totalWord
print(totalWord, "{:.2f}".format(totalAvg))