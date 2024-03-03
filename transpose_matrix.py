def transpose_matrix(matrix, m, n):
    result_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            transpose = matrix[j][i]
            row.append(transpose)
        result_matrix.append(row)
    return result_matrix

def read_matrix(n):
    num_matrix = []
    for i in range(n):
        matrix = list(map(int, input().split()))
        num_matrix.append(matrix)
    return num_matrix

def main():
    m, n = list(map(int, input().split()))
    matrix = read_matrix(n)
    result_matrix = transpose_matrix(matrix, m, n)
    # print(result_matrix)
    for i in range(len(result_matrix)):
        print(*result_matrix[i])
main()