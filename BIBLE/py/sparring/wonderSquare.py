from sys import stdin


def lenghtToCenter(x, y, size):
    A = (size // 2, size // 2)
    B = (x, y)
    return max(abs(B[0] - A[0]), abs(B[1] - A[1]))


def solveWonderSquare(n):
    size = 2 * n - 1
    wonderSquare = [[(lenghtToCenter(i, j, size) + 1) for j in range(size)] for i in range(size)]
    return wonderSquare


def printWonderSquare(wonderS):
    for row in wonderS:
        print(''.join(map(str, row)))


def main():
    n = int(stdin.readline().strip())
    printWonderSquare(solveWonderSquare(n))


main()
