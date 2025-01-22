from sys import stdin

def printer(matrix):
    [print(''.join(map(str, matrix[row][1:-1:]))) for row in range(1, len(matrix)-1)]

def solver(matrix, m, n):
    Base_matrix = [[0 for j in range(int(n) + 2)] for i in range(int(m) + 2)]
    k = 0
    for i in range(int(m)):
        k += 1
        p = 0
        for j in range(int(n)):
            p += 1
            if matrix[i][j] == '*':
                Base_matrix[k][p] = '*'
                if Base_matrix[k][p - 1] != '*':
                    Base_matrix[k][p - 1] += 1
                if Base_matrix[k + 1][p - 1] != '*':
                    Base_matrix[k + 1][p - 1] += 1
                if Base_matrix[k + 1][p] != '*':
                    Base_matrix[k + 1][p] += 1
                if Base_matrix[k + 1][p + 1] != '*':
                    Base_matrix[k + 1][p + 1] += 1
                if Base_matrix[k][p + 1] != '*':
                    Base_matrix[k][p + 1] += 1
                if Base_matrix[k - 1][p + 1] != '*':
                    Base_matrix[k - 1][p + 1] += 1
                if Base_matrix[k - 1][p] != '*':
                    Base_matrix[k - 1][p] += 1
                if Base_matrix[k - 1][p - 1] != '*':
                    Base_matrix[k - 1][p - 1] += 1
    return Base_matrix

def main():
    m, n = (stdin.readline()).split()
    case_number = 1
    while int(m) != 0 and int(n) != 0:
        matrix = []
        matrix += [list((stdin.readline().strip())) for row in range(int(m))]
        print()
        print("Field #{}:".format(case_number))
        printer(solver(matrix, m, n))
        m, n = (stdin.readline().strip()).split()
        case_number += 1

main()