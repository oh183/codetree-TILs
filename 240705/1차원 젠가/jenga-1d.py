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
    for s, e in commands:
        for idx in range(len(Blocks) - s, len(Blocks) - e, -1):
            Blocks[idx] = 0

# update the block
def update():
    global Blocks
    temp = []
    for val in Blocks:
        if val > 0:
            temp.append(val)
    Blocks = temp

def printt():
    for i in Blocks:
        if i != 0:
            print(i)

for i in range(len(commands)):
    clean()
    update()
print(len(Blocks))
printt()