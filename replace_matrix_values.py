def replace_matrix_elements(matrix, x, y):
    index_of_x = 0
    for row in matrix:
        if x in row:
            index_of_x = row.index(x)
            row[index_of_x] = y 
    return matrix

def read_matrix(n):
    num_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        num_matrix.append(row)
    return num_matrix

def main():
    m, n = list(map(int, input().split()))
    matrix = read_matrix(n)
    x, y = list(map(int, input().split()))
    result_matrix = replace_matrix_elements(matrix, x, y)
    for item in result_matrix:
        print(*item)
main()
