#!/usr/bin/env python3

def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c' and char.lower() != 'C':
            result += char

    return result
