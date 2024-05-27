string, num_q = map(str, input().split())

questions = [
    input().replace(" ", "") for _ in range(int(num_q))
]

# Replace operation
result = list(string)

for question in range(int(num_q)):
    if questions[question][0] == '1':
        # swap a th <-> b th
        a = int(questions[question][1]) - 1
        b = int(questions[question][2]) - 1
        temp = result[a]
        result[a] = result[b]
        result[b] = temp
        print(''.join(result))
    
    if questions[question][0] == '2': 
        # replace all a to b
        a = questions[question][1]
        b = questions[question][2]
        
        for idx, ch in enumerate(result):
            if ch == a:
                result[idx] = b

        # update the result 
        print(''.join(result))