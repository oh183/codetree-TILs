# get n 
n = int(input())

# get other inputs
array = str(input()).replace(" ", "")

for idx, char in enumerate(array):
    if (idx + 1) % 5 == 0:
        print(char, end = "") 
        print()
    else:
        print(char, end = "")