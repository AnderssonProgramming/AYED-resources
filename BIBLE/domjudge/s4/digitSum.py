from sys import stdin


def superDigit(num, k):
    suma = sum(map(int, list(num))) * k
    if len(str(suma)) == 1:
        return suma
    else:
        return superDigit(str(suma), 1)


def main():
    digits = stdin.readline().strip().split()
    while digits:
        print(superDigit(digits[0], int(digits[1])))
        digits = stdin.readline().strip().split()


main()
