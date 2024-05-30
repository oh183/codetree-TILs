def recursion(n):
    if n == 0:
        return 0
    
    return recursion(n - 1) + n

n = int(input())
print(recursion(n))