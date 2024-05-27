# get input
myarray = []
for _ in range(3):
    myarray.append(str(input()))

print(len(min(myarray)) - len(max(myarray)))