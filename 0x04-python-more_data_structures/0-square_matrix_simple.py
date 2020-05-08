#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return(list(map(lambda x: [y ** 2 for y in x], matrix)))
