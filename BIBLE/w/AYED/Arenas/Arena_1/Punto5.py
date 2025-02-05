from sys import stdin


def one_square(matrix, r1, r2, c1, c2, count):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if matrix[i][j] == 1:
                continue
            elif matrix[i][j] == 0:
                matrix[i][j] = 1
                count += 1
    return count


def cero_matrix(m, n):
    matrix = [[0 for j in range(n)] for i in range(m)]
    return matrix


def main():
    line = (stdin.readline().strip()).split()
    m, n, w = map(int, line)
    while m != 0 and n != 0 and w != 0:
        count = 0
        matrix = cero_matrix(m, n)
        while w > 0:
            r1, c1, r2, c2 = map(int, stdin.readline().strip().split())
            r1 = r1 - 1
            c1 = c1 - 1
            r2 = r2 - 1
            c2 = c2 - 1
            r1, r2 = min(r1, r2), max(r1, r2)
            c1, c2 = min(c1, c2), max(c1, c2)
            count = one_square(matrix, r1, r2, c1, c2, count)
            w -= 1
        void = (m * n) - count
        if void == 0:
            print('There is no empty spots.')
        elif void == 1:
            print('There is one empty spots.')
        else:
            print('There is', void, 'empty spots.')
        none = line
        m, n, w = map(int, line)
        if w == 0:
            void = m * n
            print("There are", void, "empty spots.")
            stdin.readline()
        else:
            continue


if __name__ == '__main__':
    main()
