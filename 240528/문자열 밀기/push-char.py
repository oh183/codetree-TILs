# get string 
string = list(input())

# shift to right by 1
a = string.pop(0)
string.append(a)
# print
print(''.join(string))