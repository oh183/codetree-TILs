# two words as input
first, second = map(str, input().split())

if len(first) > len(second):
    print(first, len(first))
elif len(first) == len(second):
    print("same")
else:
    print(second, len(second))