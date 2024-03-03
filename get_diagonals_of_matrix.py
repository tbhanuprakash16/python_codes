def get_diagonal_of_matrix(matrix):
    result_list = []
    for i in range(len(matrix)):
        result_list.append(matrix[i][i])
    return result_list

def read_matrix(n):
    num_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        num_matrix.append(row)
    return num_matrix

def main():
    m, n = list(map(int, input().split()))
    matrix = read_matrix(n)
    diagonal_list = get_diagonal_of_matrix(matrix)
    print(diagonal_list)
main()
