#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


# Example usage:
my_list = [1, 2, 3, 4, 5]

result_valid = element_at(my_list, 2)
print(result_valid)

result_negative = element_at(my_list, -1)
print(result_negative)

result_out_of_range = element_at(my_list, 10)
print(result_out_of_range)
