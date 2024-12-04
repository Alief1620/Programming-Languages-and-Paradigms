import numpy as np

def validate_addition(matrix1, matrix2):
    return matrix1.shape == matrix2.shape

def validate_multiplication(matrix1, matrix2):
    return matrix1.shape[1] == matrix2.shape[0]

def transpose_matrix(matrix):
    return matrix.T

def perform_operation(matrix1, matrix2, operation):
    if operation == 'add':
        if validate_addition(matrix1, matrix2):
            return matrix1 + matrix2
        else:
            raise ValueError("macierze maja rozne wymiary, nie mozna ich dodac")
    elif operation == 'multiply':
        if validate_multiplication(matrix1, matrix2):
            return matrix1.dot(matrix2)
        else:
            raise ValueError("macierze nie maja odpowiednich wymiarow do mnozenia")
    elif operation == 'transpose':
        return transpose_matrix(matrix1)
    else:
        raise ValueError("nieznana operacja")

def execute_operation(operation_str, matrix1_str, matrix2_str=None):
    matrix1 = eval(matrix1_str)
    if matrix2_str:
        matrix2 = eval(matrix2_str)
        return perform_operation(matrix1, matrix2, operation_str)
    else:
        return perform_operation(matrix1, None, operation_str)

matrix1_str = 'np.array([[1, 2], [3, 4]])'
matrix2_str = 'np.array([[5, 6], [7, 8]])'

operation = 'add'
try:
    result_add = execute_operation(operation, matrix1_str, matrix2_str)
    print("wynik dodawania:\n", result_add)
except Exception as e:
    print(e)

operation = 'multiply'
try:
    result_multiply = execute_operation(operation, matrix1_str, matrix2_str)
    print("wynik mnozenia:\n", result_multiply)
except Exception as e:
    print(e)

operation = 'transpose'
try:
    result_transpose = execute_operation(operation, matrix1_str)
    print("wynik transponowania:\n", result_transpose)
except Exception as e:
    print(e)
