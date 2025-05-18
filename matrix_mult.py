# Author: Kevin Phillips
# GitHub username: kcook555
# Date: 5/17/2025
# Description: Function dot_prod that multiplies
#              lists of numbers and function matrix_mult
#              that multiplies matrices

def dot_prod(list1, list2):
    """Return the dot product of two lists."""
    print(f'{list1} || {list2}')
    if len(list1) != len(list2):
        return None
    dot_product = 0
    for index in range(len(list1)):
        dot_product += list1[index] * list2[index]
    return dot_product

def matrix_mult(matrix1, matrix2):
    """Return the dot product of two matrices."""
    return_matrix = [[] for _ in range(len(matrix1))]
    inverted_matrix2 = [[] for _ in range(len(matrix2[0]))]
    # matrix1 needs to have the same number of rows as matrix2 columns
    if len(matrix1[0]) != len(matrix2):
        return None
    # Make an inverted matrix2 so that rows are columns and columns are rows
    for row in range(len(matrix2)):
        for column in range(len(matrix2[row])):
            inverted_matrix2[column].append(matrix2[row][column])
            print(inverted_matrix2)
    print(inverted_matrix2)
    for row in range(len(matrix1)):
        # These were originally columns in matrix2. Technically they are now rows, but
        # we don't want 2 variables called row
        for column in range(len(inverted_matrix2)):
            return_matrix[row].append(dot_prod(matrix1[row], inverted_matrix2[column]))
    return return_matrix
