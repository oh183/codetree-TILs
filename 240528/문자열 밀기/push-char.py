# get string 
string = str(input())

# shift to right by 1
string = string[1:-1] + string[-1] + string[0]

# print
print(string)