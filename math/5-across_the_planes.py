#!/usr/bin/env python3
matrix_shape = __import__('2-size_me_please').matrix_shape

def add_matrices2D(mat1, mat2):
    
    if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
        return None
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    
    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        new_mat.append(row)
    return new_mat