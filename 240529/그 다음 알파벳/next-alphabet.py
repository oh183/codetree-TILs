character = ord(str(input()))

if character < ord('z'):
    character += 1 
else:
    character = ord('a')

print(chr(character))