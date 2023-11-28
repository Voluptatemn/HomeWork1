'''
input an augmented matrix, produce the solution set if one exact solution, vector form if infinite, none if none
input uses numpy as such:
[[3, 3, 3], [2, 2, 2], [1, 1, 1]] is a 3 by 2 matrix 
'''

import numpy as np

def replacement(matrix, row1, row2):
    matrix[row1] += matrix[row2]
    return matrix

def interchange(matrix, row1, row2):
    store = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = store
    return matrix

def scaling(matrix, row, scale):
    matrix[row] *= scale
    return matrix

matrix = np.array([[3, 3, 3, 3], [2, 2, 2, 4], [1, 1, 1, 5]])
print(matrix.shape[1])
print(scaling(matrix, 1, 3))

def calculation(matrix):
    row, column = matrix.shape
    
        