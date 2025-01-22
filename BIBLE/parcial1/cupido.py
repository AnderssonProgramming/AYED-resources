# Nombre: Juan Camilo Bazurto Arias
# Carné: 2167888
# Documento: 1000521079

from sys import stdin
import math


def cupido(alturasP, altura):
    mid = len(alturasP) // 2
    if len(alturasP) == 0:
        return -math.inf
    if alturasP[mid] >= altura:
        return cupido(alturasP[:mid], altura)
    return max(alturasP[mid], cupido(alturasP[mid + 1:], altura))


def main():
    cant = stdin.readline().strip()
    cant = int(cant)
    alturasP = stdin.readline().strip().split()
    for p in range(cant):
        alturasP[p] = int(alturasP[p])
    consult = stdin.readline().strip()
    consult = int(consult)
    alturas = stdin.readline().strip().split()
    for c in range(consult):
        print(cupido(alturasP, int(alturas[c])) if cupido(alturasP, int(alturas[c])) != -math.inf else 'X')


main()
