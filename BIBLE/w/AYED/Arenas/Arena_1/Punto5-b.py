from sys import stdin


def main():
    n, m, w = map(int, stdin.readline().strip().split())
    while n != 0 and m != 0 and w != 0:
        count = 0
        matrix = [[0 for j in range(m)] for i in range(n)]
        while w > 0:
            r1, c1, r2, c2 = map(int, stdin.readline().strip().split())
            r1 -= 1
            c1 -= 1
            r2 -= 1
            c2 -= 1
            r1, r2 = min(r1, r2), max(r1, r2)
            c1, c2 = min(c1, c2), max(c1, c2)
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if matrix[i][j] == 1:
                        continue
                    elif matrix[i][j] == 0:
                        matrix[i][j] = 1
                        count += 1
            w -= 1
        void = (m * n) - count
        if void == 0:
            print("There is no empty spots.")
        elif void == 1:
            print("There is one empty spot.")
        else:
            print("There are", void, "empty spots.")
        none = stdin.readline().strip().split()
        n, m, w = stdin.readline().strip().split()
        n = int(n)
        m = int(m)
        w = int(w)
        if w == 0:
            void = m*n
            print("There are", void, "empty spots.")
            stdin.readline()
        else:
            continue


main()