def add_matrices(mat1, mat2):
    a = len(mat1)
    b = len(mat2)
    if a == b:
        addition_matrix = []
        for i in range(a):
            row = []
            for j in range(b):
                add = mat1[i][j] + mat2[i][j]
                row.append(add)
            addition_matrix.append(row)
    return addition_matrix

def read_matrix(n):
    num_matrix = []
    for i in range(n):
        matrix = list(map(int, input().split()))
        num_matrix.append(matrix)
    return num_matrix

def main():
    m, n = list(map(int, input().split()))
    matrix_1 = read_matrix(m)
    matrix_2 = read_matrix(n)
    result_matrix = add_matrices(matrix_1, matrix_2)
    for i in range(len(result_matrix)):
        print(*result_matrix[i])
main()