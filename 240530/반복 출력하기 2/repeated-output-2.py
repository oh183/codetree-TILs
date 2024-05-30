def practice_recursion(n):
    if n == 0:
        return 
    
    practice_recursion(n-1)
    print("HelloWorld")

n = int(input())
practice_recursion(n)