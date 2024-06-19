pairs = input()
stack = []

flag = 1
counter = 0

for idx, val in enumerate(pairs):
    if val == "(":
        for i in range(idx, len(pairs)):
            if pairs[i] == ")":
                counter += 1
print(counter)