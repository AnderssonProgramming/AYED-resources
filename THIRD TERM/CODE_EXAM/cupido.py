from sys import stdin
import math
def cupido(alturaPrincesas,altura):

    mitad = len(alturaPrincesas) // 2

    if len(alturaPrincesas) == 0:
        return -math.inf

    if alturaPrincesas[mitad] >= altura:
        return cupido(alturaPrincesas[:mitad],altura)

    return max(alturaPrincesas[mitad],cupido(alturaPrincesas[mitad + 1:],altura))

def main():
    princesas = int(stdin.readline().strip())
    alturaPrincesas = stdin.readline().strip().split()

    for i in range(princesas):
        alturaPrincesas[i] = int(alturaPrincesas[i])

    consultas = int(stdin.readline().strip())
    alturas = stdin.readline().strip().split()

    for j in range(consultas):
        print(cupido(alturaPrincesas,int(alturas[j])) if cupido(alturaPrincesas,int(alturas[j])) != -math.inf else "X" )
main()