from sys import stdin


def transfor(i, j):
    return i + 1, j + 1


def calcularProxim(campo, fila, colum):
    coord = transfor(fila, colum)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and campo[coord[0] + i][coord[1] + j] != '*':
                campo[coord[0] + i][coord[1] + j] += 1
    campo[coord[0]][coord[1]] = '*'


def calcularCampo(campo, filas, colums):
    campo2 = [[0 for j in range(colums + 2)] for i in range(filas + 2)]
    for fila in range(filas):
        for colum in range(colums):
            if campo[fila][colum] == '*':
                calcularProxim(campo2, fila, colum)
    return campo2


def printCampo(campo):
    campo2 = campo[1:len(campo) - 1]
    for fila in campo2:
        print(''.join(map(str, fila[1:len(fila) - 1])))


def output(mensaje, index, campo):
    print(mensaje.format(index))
    printCampo(campo)
    print()


def main():
    mensaje, index = 'Field #{}:', 1
    filas, colums = map(int, stdin.readline().strip().split())
    while filas != 0 or colums != 0:
        campo = []
        for fila in range(filas):
            campo.append(stdin.readline().strip())
        output(mensaje, index, calcularCampo(campo, filas, colums))
        index += 1
        filas, columns = map(int, stdin.readline().strip().split())


main()
