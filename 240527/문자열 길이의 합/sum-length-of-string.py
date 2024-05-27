# get n
n = int(input())

# get other inputs
myArray = [
    input() for _ in range(n)
]

# get total length, total number of words starts with 'a' 
total = 0 
ctr = 0
for i in myArray:
    if i[0] == 'a':
        ctr += 1
    total += len(i)

print(total, ctr)