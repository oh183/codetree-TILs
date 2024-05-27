myInput = input().split()

for idx, word in enumerate(myInput):
    if (idx + 1) % 2 != 0:
        print(word)