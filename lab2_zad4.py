from functools import reduce


def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def matrix_multiplication(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2[0]))] for i
            in range(len(matrix1))]


def apply_matrix_operations(matrices, operation):
    return reduce(operation, matrices)


matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]
matrix3 = [
    [9, 10],
    [11, 12]
]

matrices = [matrix1, matrix2, matrix3]

result_addition = apply_matrix_operations(matrices, matrix_addition)
print("Suma macierzy:")
for row in result_addition:
    print(row)

result_multiplication = apply_matrix_operations(matrices, matrix_multiplication)
print("\nIloczyn macierzy:")
for row in result_multiplication:
    print(row)
