string = list(input())

length = len(string) - 1

string[1] = 'a'
string[length - 1] = 'a'

print(''.join(string))