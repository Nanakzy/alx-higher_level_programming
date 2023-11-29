#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char


        print(uppercase_char, end='')
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
