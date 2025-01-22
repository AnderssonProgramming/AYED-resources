# -*- coding: utf-8 -*-
def leer_datos():
    with open('entrada3.txt', 'r') as f:
        lineas = f.readlines()
        return [list(map(int, linea.strip().split())) for linea in lineas]         #Leer los dos números, ya sea por espacio o coma

def maximo_comun_divisor(i, j):
    while j != 0:
        i, j = j, i % j
    return i

def escribir_MCD(MCDs):
    with open('salida3.txt', 'w') as f:
        for MCD in MCDs:
            f.write(str(MCD) + '\n')

def main():
    print("Determinar el MCD de dos números enteros i,j : ")
    datos = leer_datos()
    MCDs = []

    for i, j in datos:
        MCD = maximo_comun_divisor(i, j)
        MCDs.append(MCD)

    escribir_MCD(MCDs)


main()
