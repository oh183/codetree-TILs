array = [
    input() for _ in range(10)
]

endString = str(input())

for word in array:
    if word[-1] == endString:
        print(word)