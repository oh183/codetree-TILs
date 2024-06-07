n = int(input())

def recursion(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    

    return recursion(n - 1) + recursion(n - 2)

print(recursion(n))