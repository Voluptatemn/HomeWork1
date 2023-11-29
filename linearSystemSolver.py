'''
input an augmented matrix, produce the solution set if one exact solution, vector form if infinite, none if none
input uses numpy as such:
[[3, 3, 3], [2, 2, 2], [1, 1, 1]] is a 3 by 2 matrix 
'''

import numpy as np

def copy(array):
    new_array = []
    for i in range (len(array)):
        new_array.append(array[i])
    return new_array

def replacement(matrix, row1, row2):
    matrix[row1] += matrix[row2]
    return matrix

def interchange(matrix, row1, row2):
    store = copy(matrix[row1])
    matrix[row1] = matrix[row2]
    matrix[row2] = store
    return matrix

def scaling(matrix, row, scale):
    matrix[row] *= scale
    return matrix

matrix = np.array([[0, 3, 3, 3], [2, 2, 2, 4], [1, 1, 1, 5]])
print(matrix)
# print(interchange(matrix, 0, 1))

def calculation(matrix, index):
    row, column = matrix.shape
    
    # loop through the row to move the row with non zero Xo to row o
    for i in range (index, row):
        if matrix[i][index] != 0:
            interchange(matrix, i, index)
            break       
    
    # check if there is any row with a non-zero leading number
    if matrix[index][index] == 0:
        return calculation(matrix, index + 1)
    
    
    
    
    return 

calculation(matrix, 0)
    
        