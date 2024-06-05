def recursion(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return recursion(n // 2) + 1
    else:
        return recursion(n // 3) + 1

n = int(input())
print(recursion(n))