#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    
    if len(mat1[0]) != len(mat2):
        return None
    
    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum_item = 0
            for k in range(len(mat1[0])):
                sum_item += mat1[i][k]*mat2[k][j]
            row.append(sum_item)
        new_mat.append(row)
    return new_mat