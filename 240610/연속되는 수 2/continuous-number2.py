n = int(input())
arr = [int(input()) for _ in range(n)]
num_freq = [1] * 1001
counter = 0

for i in range(len(arr)):
    if i == 0 or arr[i] == arr[i - 1]:
        counter += 1
        current_number = arr[i]

    else:
        if counter > num_freq[current_number]:
            if i - 1 == 0:
                num_freq[current_number] = counter
                continue
            
            if counter > 0:
                num_freq[current_number] = counter + 1

        counter = 0

print(max(num_freq))