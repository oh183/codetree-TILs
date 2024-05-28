letter = str(input())

if ord(letter) > ord('a'):
    print(chr(ord(letter) - 1))
else:
    print('z')