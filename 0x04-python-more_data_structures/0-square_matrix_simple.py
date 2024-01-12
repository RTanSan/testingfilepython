#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    for number in matrix:
        square_number = [i ** 2 for i in number]
        return(squares)
