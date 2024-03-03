def get_sum_of_upper_triangle(matrix):
    sum_of_upper_triangle = sum(matrix[0])
    for i in range(len(matrix)):
        sum_of_upper_triangle += sum(matrix[i][:-i])
    return sum_of_upper_triangle

def get_sum_of_lower_triangle(matrix):
    sum_of_lower_triangle = 0 
    for i in range(len(matrix)):
        sum_of_lower_triangle += sum(matrix[i][-i-1:])
    return sum_of_lower_triangle

def read_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    m, n = list(map(int, input().split()))
    matrix = read_matrix(n)
    sum_of_upper_triangle = get_sum_of_upper_triangle(matrix)
    sum_of_lower_triangle = get_sum_of_lower_triangle(matrix)
    print(sum_of_upper_triangle)
    print(sum_of_lower_triangle)
main()