#!/usr/bin/env python3

def cat_arrays(arr1, arr2):
    
    new_arr = [*arr1]
    for i in range(len(arr2)):
        
        new_arr.append(arr2[i])
    return new_arr