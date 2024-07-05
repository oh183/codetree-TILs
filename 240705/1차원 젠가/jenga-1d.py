# 블럭빼기

n = int(input())
Blocks = []
for i in range(n):
    Blocks.append(int(input()))

commands = [ 
    list(map(int, input().split())) for _ in range(2)
]

# remove block 
def clean():
    global Blocks
    Blocks.reverse()
    for start, end in commands:
        for idx in range(start - 1, end):
            Blocks[idx] = 0
    Blocks.reverse()

# update 
def update():
    global Blocks
    temp = []
    for i in Blocks:
        if i > 0:
            temp.append(i)
    Blocks = temp

# print
def pprint():
    for i in Blocks:
        print(i)


for _ in range(len(commands)):
    clean()
    update()
print(len(Blocks))
pprint()