commands = list(map(int, input().split()))

# a, c -> hour
# b, d -> minutes
a = commands[0]
b = commands[1]
c = commands[2]
d = commands[3]

hour_max = 60
min_max = 60
total = 0 
while True:
    if d >= b:
        # simple case without borrowing 
        total = d - b + 60 * (c-a)
        break 
    else:
        # we need borrowing 
        # 1. decrement the hour 
        c -= 1
        d += 60
        total = d - b + 60 * (c-a)
        break
print(total)