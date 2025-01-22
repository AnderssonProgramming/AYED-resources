from sys import stdin


def super_Digit(p):
    if len(p) == 1:
        return int(p)
    else:
        suma = sum(map(int, list(p)))
        return super_Digit((str(suma)))


def main():
    line = stdin.readline().strip()
    while line:
        n, k = line.split()
        sd = n * int(k)
        print(super_Digit(sd))
        line = stdin.readline().strip()


if __name__ == '__main__':
    main()
