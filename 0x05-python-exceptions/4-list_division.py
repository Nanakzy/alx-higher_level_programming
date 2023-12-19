#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0
            result = value_1 / value_2
        except (ZeroDivisionError, TypeError):
            if all(isinstance(value, (int, float)) for value in (value_1, value_2)):
                result = 0
            elif not isinstance(value_1, (int, float)):
                print("wrong type")
            elif value_2 == 0:
                print("division by 0")
            else:
                print("out of range")
            result = 0
        finally:
            result_list.append(result)

    return result_list
