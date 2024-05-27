wordBank = ["apple", "banana", "grape", "blueberry", "orange"]
charInput = str(input())
ctr = 0 

for word in wordBank:
    for idx, char in enumerate(word):
        if charInput == char and (idx == 2 or idx == 3):
            print(word)
            ctr += 1 
            break

print(ctr)