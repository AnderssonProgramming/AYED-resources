from sys import stdin


def counter(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + counter(n//2)
        else:
            return 1 + counter(3*n+1)


def main():
    try:
        i, j = map(int, stdin.readline().strip().split())
        while i != '' or j != '':
            cycles = []
            for cycle in range(min(i,j), max(i,j) + 1):
                contador = counter(cycle)
                cycles += [contador]
            print(i, j, max(cycles))
            i, j = map(int, stdin.readline().strip().split())
    except ValueError:
        return
main()
