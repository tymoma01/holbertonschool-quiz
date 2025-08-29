#!/usr/bin/env python3

def matrix_shape(matrix):
    res =[len(matrix)]
    while isinstance(matrix[0], list):
        res.append(len(matrix[0]))
        matrix = matrix[0]
    return res