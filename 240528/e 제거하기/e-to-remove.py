# original input
string = str(input())

# find the index
index = string.find('e')

# convert to list
string = list(string)

# remove the element by using pop()
string.pop(index)

# print
print(''.join(string))