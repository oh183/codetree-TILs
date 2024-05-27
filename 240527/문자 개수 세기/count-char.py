first = str(input())
second = str(input())
counter = 0

for character in first:
    if character == second:
        counter += 1

print(counter)