#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
character = 'a'
if islower(character):
    print('True')
else:
    print('False')
