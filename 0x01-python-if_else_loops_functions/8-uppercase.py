#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        result_str += uppercase_char


    print("{}".format(result_str))

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
