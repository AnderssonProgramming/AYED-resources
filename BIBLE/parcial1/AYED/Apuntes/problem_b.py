from sys import stdin


def solve(matrix, n, m):
    blankMatrix = [[0 for j in range(m + 2)] for i in range(n + 2)]
    # Primeros
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '*':
                blankMatrix[i + 1][j + 1] = '*'
                # Se cambian valores alrededor del *
                for new_i in range(i, i + 3):
                    for new_j in range(j, j + 3):
                        if new_i == i + 1 and new_j == j + 1:
                            continue
                        else:
                            try:
                                blankMatrix[new_i][new_j] += 1
                            except:
                                continue
    return blankMatrix


def pretty_print_mat(matrix):
    for row in range(1, len(matrix) - 1):
        print(''.join(map(str, matrix[row][1:-1:])))


def main():
    mn = (stdin.readline().strip()).split()
    case = 1
    # Iniciación: Las dimensiones de la matriz deben ser > 0 para que esta se pueda usar
    while int(mn[0]) > 0 and int(mn[1]) > 0:
        # Estabilidad: Para que se continue en el ciclo la matriz debe cumplir la condicion base
        matrix = []
        for row in range(int(mn[0])):
            line = stdin.readline().strip()
            # Se guardan las filas en un arreglo
            matrix += [list(line)]
        print('Field #{}:'.format(case))
        pretty_print_mat(solve(matrix, int(mn[0]), int(mn[1])))
        print()
        mn = (stdin.readline().strip()).split()
        case += 1

main()