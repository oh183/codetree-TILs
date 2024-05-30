numberOne, numberTwo = map(str, input().split())

concat = numberOne+numberTwo
revconcat = numberTwo+numberOne

print(int(concat) + int(revconcat))