from sys import stdin


def matrix(lista_in, lista_pre):
    matriz = [["_" for x in range(len(lista_in) + 1)] for y in range(len(lista_in) + 1)]
    return matriz[0]

def main():
    read = stdin.readline().strip()
    lista_in = list(read)
    lista_pre = list(read)
    print(matrix(lista_in, lista_pre))