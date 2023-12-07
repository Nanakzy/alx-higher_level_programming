#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            if isinstance(value, (int, float)):
                new_row.append(value * value)
            else:
                new_row.append(value)
            new_matrix.append(new_row)
            return new_matrix
