from sys import stdin


def cartas(lista):
    new = []
    while len(lista) > 1:
        aux = lista[0]
        new += [aux]
        lista.pop(0)
        aux = lista[0]
        lista.pop(0)
        lista.append(aux)
    return new


def main():
    linea = int(stdin.readline().strip())

    while linea != 0:
        lista = [n for n in range(1, linea + 1)]
        print("Discarded cards:", ", ".join(map(str, cartas(lista))))
        print("Remaining card:", lista[0])
        linea = int(stdin.readline().strip())


main()
