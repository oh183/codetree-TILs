array = [
    input() for _ in range(10)
]

endString = str(input())
ctr = 0 

for word in array:
    if word[-1] == endString:
        print(word)
        ctr += 1

if ctr == 0:
    print('None')