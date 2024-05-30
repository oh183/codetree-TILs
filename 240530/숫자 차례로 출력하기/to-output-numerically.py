def oneToN(n):
    if n == 0:
        return
    
    oneToN(n-1)
    print(n, end =" ")

def nToOne(n):
    if n == 0:
        return

    print(n, end= " ")
    nToOne(n-1)

n = int(input())
oneToN(n)
print()
nToOne(n)