#!/usr/bin/python3
"""
ROtating a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a matrix 90 degrees clockwise in place.
    Args:
    matrix (list of list of int): The n x n 2D matrix to rotate
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap element at (i, j) with element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        # Reverse the ith row
        matrix[i].reverse()
