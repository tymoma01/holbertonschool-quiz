#!/usr/bin/env python3

def matrix_transpose(matrix):
    
    t_matrix = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        t_matrix.append(row)
    return t_matrix