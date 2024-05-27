# get the input
first, second = map(str, input().split())

# replace 
target = first[0:2]
newArr = list(second)
newArr[0:2] = target

# join again
print(''.join(newArr))