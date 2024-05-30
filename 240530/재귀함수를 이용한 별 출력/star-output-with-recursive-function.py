def recursive(n):
    if n == 0:
        return 
    
    recursive(n-1)
    print('*' * n)

n = int(input())
recursive(n)