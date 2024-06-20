binary = input()

def binary_to_decimal(number):
    reversedString = number[::-1]
    result = 0 

    for idx, val in enumerate(reversedString):
        result += int(val) * pow(2, idx)    
    return result

MaxVal = [0]

for idx, val in enumerate(binary):
    if val == '0':
        tempNumber = binary[:idx] + '1' + binary[idx + 1:]
        MaxVal.append(binary_to_decimal(tempNumber))

print(max(MaxVal))