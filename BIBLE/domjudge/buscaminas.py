from sys import stdin


def calcularProximidad(matriz, fila, colum):
    if fila != 0 and colum != len(matriz[fila]) - 1:
        campo2 = matriz[fila - 1: fila + 2]
        campo3 = []
        for fila in campo2:
            if colum == 0:
                for i in range(colum, colum + 2):
                    campo3.append(fila[i])

            else:
                for i in range(colum - 1, colum + 2):
                    campo3.append(fila[i])
        if '*' in campo3:
            num = campo3.count('*')
            return num
        else:
            return 0
    elif fila == 0 and colum != len(matriz[fila]) - 1:
        campo2 = matriz[fila: fila + 2]
        campo3 = []
        for fila in campo2:
            if colum == 0:

                for i in range(colum, colum + 2):
                    campo3.append(fila[i])
            else:
                for i in range(colum - 1, colum + 2):
                    campo3.append(fila[i])
        if '*' in campo3:
            num = campo3.count('*')
            return num
        else:
            return 0
    elif colum == len(matriz[fila]) - 1:
        campo2 = matriz[fila - 1: fila + 2]
        campo3 = []
        for fila in campo2:
            for i in range(colum - 1, colum + 1):
                campo3.append(fila[i])
        if '*' in campo3:
            num = campo3.count('*')
            return num
        else:
            return 0
    else:
        return 0


def calculateMatrix(matriz, filas, columns):
    nCampo = [[0 for i in range(columns)] for j in range(filas)]
    for i in range(filas):
        for j in range(columns):
            if matriz[i][j] != '*':
                nCampo[i][j] += calcularProximidad(matriz, i, j)
            else:
                nCampo[i][j] = '*'
    return nCampo


def outputMatrix(index, matrix):
    print("Field #{}:".format(index))
    for fila in matrix:
        for x in fila:
            print(x, end="")
        print()
    print()

def main():
    index = 1
    filas, columns = map(int, stdin.readline().strip().split())
    while filas != 0 or columns != 0:
        campo = []
        for fila in range(filas):
            campo.append(stdin.readline().strip())
        outputMatrix(index, calculateMatrix(campo, filas, columns))
        index += 1
        filas, columns = map(int, stdin.readline().strip().split())


main()
