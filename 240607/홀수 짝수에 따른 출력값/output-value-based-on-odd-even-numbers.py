n = int(input())

def recursion(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        # even number
        return recursion(n-1)
    else:
        return recursion(n-1) + n


print(recursion(n))