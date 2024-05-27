# get input
myarray = []
for _ in range(3):
    myarray.append(list(map(str, input())))

largest = min(myarray)
smallest = max(myarray)

print(len(largest) - len(smallest))