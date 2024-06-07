n, k = map(int, input().split())

# create 1D array
result = [0] * n


for _ in range(k):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    while start <= end:
        result[start] += 1 
        start += 1     

print(max(result))