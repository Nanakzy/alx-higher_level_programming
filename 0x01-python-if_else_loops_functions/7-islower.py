#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
character = 'g'
if islower(character):
    print('True')
else:
    print('False')
