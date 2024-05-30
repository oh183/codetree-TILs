def recursion(n):
    if n == 0:
        return
    
    print(n, end= " ")
    recursion(n -1)
    print(n, end = " ")

n = int(input())
recursion(n)