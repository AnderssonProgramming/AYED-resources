#Gutierrez Laura - Cupido

from sys import stdin
import math

def cupido(alturasPrincesas, altura):
    mitad = len(alturasPrincesas) // 2
    if len(alturasPrincesas) == 0:
        return -math.inf
    if alturasPrincesas[mitad] >= altura:
        return cupido(alturasPrincesas[:mitad], altura)
    return max(alturasPrincesas[mitad], cupido(alturasPrincesas[mitad + 1:], altura))

def main(): 
    princesas = int(stdin.readline().strip())
    alturasPrincesas = stdin.readline().strip().split()
    for i in range(princesas):
        alturasPrincesas[i] = int(alturasPrincesas[i])
    consultas = int(stdin.readline().strip())
    alturas = stdin.readline().strip().split()
    for j in range(consultas):
        print(cupido(alturasPrincesas, int(alturas[j])) if cupido(alturasPrincesas, int(alturas[j])) != -math.inf else 'X')

main()
