def multiply_matrices(mat1, mat2):
    result_matrix = []
    if len(mat1) != len(mat2[0]):
        print("Matrices Cannot Multiply")
        return None 
    
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            multiply = 0
            for k in range(len(mat2)):
                multiply += mat1[i][k] * mat2[k][j]
            row.append(multiply)
        result_matrix.append(row)
    return result_matrix

def read_matrix(n):
    num_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        num_matrix.append(row)
    return num_matrix

def main():
    m, n = list(map(int, input().split()))
    matrix_1 = read_matrix(m)
    matrix_2 = read_matrix(n)
    result_matrix = multiply_matrices(matrix_1, matrix_2)
    for i in range(len(result_matrix)):
        print(*result_matrix[i])
main()
