#!/usr/bin/python3
"""
0-Pascal's Triangle
"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            # First row is always [1]
            row = [1]
        else:
            # Generate current row based on the previous row
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)

        triangle.append(row)

    return triangle
