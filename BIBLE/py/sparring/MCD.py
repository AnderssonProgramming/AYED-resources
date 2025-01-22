from sys import stdin


def MCD(i, j):
    while j >= 2:
        c = i % j
        i, j = j, c
    if j == 0:
        return i
    else:
        return 1


def main():
    i, j = map(int, stdin.readline().strip().split())
    while i and j:
        print(MCD(i, j))
        i, j = map(int, stdin.readline().strip().split())


main()

