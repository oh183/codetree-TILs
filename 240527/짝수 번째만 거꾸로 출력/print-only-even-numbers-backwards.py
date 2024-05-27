# Get input
myString = str(input())
revString = ""
# calculate
for idx, char in enumerate(myString):
    if (idx + 1) % 2 == 0:
        revString += char
print(revString[::-1])