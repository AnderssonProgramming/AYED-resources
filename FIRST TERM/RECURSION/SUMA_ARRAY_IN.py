"""Escribir una función recursiva que devuelva la suma de un subarreglo de N enteros,
límitado por indices (i,j)  en una lista de enteros L"""

import sys                            #Librería

def número_Elementos():
    n=-1

    while n <= 0:
        try:
            n=int(sys.stdin.readline().strip())       #número_Elementos administra la cantidad de números
        except ValueError:
            continue
    return n

def carga_numeros(n):
    lista = []
    numeros = sys.stdin.readline().strip().split()

    for i in range(n):
        try:                                                #carga_numeros administra los números
            numero = int(numeros[i])
        except ValueError:
            continue

        lista.append(numero)

    return lista

def sumaElementos(lista, i, j):                                   #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if i > j or i >= len(lista):                                  #c1             n            c1             n
        return 0                                                  #c2             1            c2             1
    else:
        return lista[i] + sumaElementos(lista, i+1, j)            #c3             n            c3             n-1
                                                                    # T(n)=O(n)                  #T(n)=Ohm(n)
def main():
    with open('entrada2.txt', 'r') as f:  # Abre el archivo 'entradas.txt' en modo lectura
        while True:
            try:
                n = int(next(f))  # Lee la cantidad de números en la prueba
                numeros = next(f).strip().split()  # Lee los números de la prueba
                lista = [int(num) for num in numeros]
                i, j = map(int, next(f).strip().split())  # Lee los índices i y j
                suma = sumaElementos(lista, i, j)
                print("La suma de los elementos entre los índices", i, "y", j, "es:", suma)
            except StopIteration:  # Cuando no hay más pruebas, termina el bucle
                break
main()
