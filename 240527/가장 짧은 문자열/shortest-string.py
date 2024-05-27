# get input
myarray = []
for _ in range(3):
    myarray.append(str(input()))

print(len(max(myarray, key = len)) - len(min(myarray, key = len)))