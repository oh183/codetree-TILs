# get input
string = str(input())

# first, second 
first = string[0]
second = string[1]

# replace
result = ""
for ch in string:
    if ch == first:
        result += second
    elif ch == second:
        result += first
    else:
        result += ch

print(result)