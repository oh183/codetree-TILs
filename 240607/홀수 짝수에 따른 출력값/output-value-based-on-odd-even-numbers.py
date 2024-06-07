n = int(input())

def odd(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        # even number
        return odd(n-1)
    else:
        return odd(n-1) + n

def even(n):
    if n == 2:
        return 2
    elif n % 2 == 0:
        # even number
        return even(n-1) + n
    else:
        return even(n-1)

if n % 2 == 0:
    print(even(n))
else:
    print(odd(n))