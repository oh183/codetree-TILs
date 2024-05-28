firstLetter, secondLetter = map(str, input().split())
print(ord(firstLetter) + ord(secondLetter), abs(ord(firstLetter) - ord(secondLetter)))