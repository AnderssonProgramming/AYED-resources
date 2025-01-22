from sys import stdin


def palin(cadena):
    cadena = list(cadena)
    cadena2 = [cadena[i] for i in range(len(cadena) - 1, -1, -1)]
    if cadena2 == cadena:
        print(True)
    else:
        print(False)


def main():
    cadena = stdin.readline().strip()
    while cadena:
        palin(cadena)
        cadena = stdin.readline().strip()


main()
