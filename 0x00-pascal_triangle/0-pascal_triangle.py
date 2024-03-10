#!/usr/bin/python3
"""
Pascal's triangle that returns a list of lists of integer.
"""

def factorial(n):
    """ Factorial function."""

    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

def comb(a, b):
    """ Calculate the combination of two numbers."""

    return factorial(a) // (factorial(b) * (factorial(a - b)))

def pascal_triangle(n):
    """ Representing the pascal's triangle of n."""

    matrix = []

    if n <= 0:
        return matrix
    for x in range(n):
        rows = []

        for y in range(x + 1):
            result = comb(x, y)
            rows.append(result)
        matrix.append(rows)
    return matrix
