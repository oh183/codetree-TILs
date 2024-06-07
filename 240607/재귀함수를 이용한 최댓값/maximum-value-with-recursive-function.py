def recursion(elements, value, i = 0):
    if i == len(elements):
        return value
    
    if elements[i] > value:
        value = elements[i]

    return recursion(elements, value, i + 1)

n = int(input())
elements = list(map(int, input().split()))
print(recursion(elements, 0))