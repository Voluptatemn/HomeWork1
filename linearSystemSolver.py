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

matrix = generate_matrix(3, 4, 0, 4)
# matrix = [[0, 1, -4, 8], [2, -3, 2, 1], [4, -8, 12, 1]]
print(matrix)

# ef 
def calculation(matrix, index):
    
    row, column = matrix.shape
    
    if index == column - 1:
        return matrix
    
    # loop through the row to move the row with non zero Xo to row o
    for i in range (index, row):
        if matrix[i][index] != 0:
            interchange(matrix, i, index)
            break       
    
    # check if there is any row with a non-zero leading number
    x = matrix[index][index]
    if x == 0:
        return calculation(matrix, index + 1)
    
    # make all other nunber at position column index to be zero
    for i in range (index+1, row):
        y = matrix[i][index]
        if y == 0:
            continue
        else:
            scaling(matrix, i, x / matrix[i][index])
            replacement(matrix, i, index)
            
    # move the iteration into the next step
    return calculation(matrix, index + 1)

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
    calculation(matrix, 0)
    print(matrix)
    if inconsistency(matrix):
        print("Inconsistent")
    else:
        rref(matrix, 0)
    return matrix

print(initiate(matrix))

    
        