#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ divide all elements of a mtrix


    Args:
    matrix (list of lists):  has integers or floats
    div (int or float): the divisor

    Returns:
    list of lists: new matrix with elements rounded to 2 decimal places

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if each row of the matrix does not have the same size,
               or if div is not a number.
    ZeroDivisionError: If div is equal to 0
    """

    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

     # Check if div is a number
     if not isinstance(div, (int, float)):
         raise TypeError("div must be a number")

      # Check if div is not equal to 0
      if div == 0:
          raise ZeroDivisionError("division by zero")

      # Divide each element of the matrix by div and round to 2 decimal places
      result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

      return result_matrix
