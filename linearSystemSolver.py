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
    matrix[row1] -= matrix[row2]
    return matrix

def interchange(matrix, row1, row2):
    store = copy(matrix[row1])
    matrix[row1] = matrix[row2]
    matrix[row2] = store
    return matrix

def scaling(matrix, row, scale):
    matrix[row] *= scale
    return matrix

# matrix = np.array([[9, 3, 3, 3], [2, 2, 2, 4], [1, 1, 5, 5]])
# print(matrix)
# print(interchange(matrix, 0, 1))

def generate_matrix(row, column, low, high):
    return np.random.random_integers(low, high, (row, column))


# ef 
def ef(matrix, column_index, row_index):
    
    row, column = matrix.shape
    
    if column_index == column - 1:
        return matrix
    
    if row_index == row:
        return matrix
    
    # find the pivot, and interchange the pivot 
    no_pivot = True
    for i in range (row_index, row):
        if matrix[i][column_index] != 0:
            interchange(matrix, i, row_index)
            no_pivot = False
        
    # if no pivot for the column, advance to the next column 
    if no_pivot:
        return ef(matrix, column_index + 1, row_index)
    
    # use row replacement to eliminate 
    x = matrix[row_index][column_index]
    for i in range (row_index + 1, row):
        y = matrix[i][column_index]
        if y == 0:
            continue
        else:
            scaling(matrix, i, x / y)
            replacement(matrix, i, row_index)
    
    # advance into next column, and next row
    return ef(matrix, column_index + 1, row_index + 1)
    

def allzero(row, consistency = 1):
    check = True
    for i in range (len(row) - consistency):
        if row[i] != 0:
            check = False
            return check
    return check

def inconsistency(matrix):
    row, column = matrix.shape
    if allzero(matrix[row - 1]) and matrix[row - 1][column - 1] != 0:
        return True
    else:
        return False
    
def leadingIndex(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i 
    
def rref(matrix, index):
    
    row, column = matrix.shape
    
    if index == row:
        return matrix
    
    currow = row - index - 1
    
    if allzero(matrix[currow], consistency = 0):
        return rref(matrix, index + 1)
    
    column_pos = leadingIndex(matrix[currow])
    x = matrix[currow][column_pos]
    scaling(matrix, currow, 1 / x)
    
    for i in range (currow):
        y = matrix[i][column_pos]
        if y == 0:
            continue
        else:
            scaling(matrix, i, 1 / y)
            replacement(matrix, i, currow)
    
    return rref(matrix, index + 1)

def initiate(matrix):
    matrix = np.asfarray(matrix)
    ef(matrix, 0, 0)
    print(matrix)
    if inconsistency(matrix):
        print("Inconsistent")
    else:
        rref(matrix, 0)
    return matrix



    
        