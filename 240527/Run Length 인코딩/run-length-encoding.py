# get input
string = str(input())

# calculate
prev = ""
result = ""
ctr = 0

prev = string[0]
for char in string:
    if char != prev:
        # save the prev string
        result += prev + str(ctr)
        # reset the counter
        ctr = 1
    else:
        ctr += 1 
    prev = char 

result += prev + str(ctr)
print(len(result))
print(result)