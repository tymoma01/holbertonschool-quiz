#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    
    if axis == 1:
        new_mat = []
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat1)):
            new_mat.append(mat1[i][:] + mat2[i][:])
        return new_mat

    else:
        return None