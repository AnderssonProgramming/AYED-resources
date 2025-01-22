"""Escriba una función recursiva que ordene de menor a mayor una lista de enteros
basándose en la siguiente idea: coloque el elemento más pequeño en la primera
ubicación, y luego ordene el resto del arreglo con una llamada recursiva. """

"""Librería para que los inputs se pongan en un archivo"""
import sys

def carga_numeros():
    lista = []
    n = int(sys.stdin.readline().strip())
    numeros = sys.stdin.readline().strip().split()
                                                     #carga_numeros administra los datos(cantidad y números)
    for i in range(n):
        try:
            numero = int(numeros[i])
        except ValueError:
            continue

        lista.append(numero)

    return lista

def menor_mayor(lista):                                     #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if len(lista) <= 1:                                     #c1             n            c1             n
        return lista                                        #c2             1            c2             1
    else:
        menorNumero = min(lista)                            #c3             1            c3             1
        lista.remove(menorNumero)                           #c4             n-1          c4             n

    return [menorNumero] + menor_mayor(lista)               #c5             1            c5             1
                                                               #T(n)=O(n)                   #T(n)=Ohm(n)
def main():
    with open('entrada.txt', 'r') as f:  # Abre el archivo 'pruebas.txt' en modo lectura
        while True:
            try:
                line = next(f).strip()  # Lee la siguiente línea y elimina los espacios en blanco
                if not line:  # Si la línea está vacía, pasa a la siguiente línea
                    continue
                n = int(line)  # Convierte la línea en un número entero
                numeros = next(f).strip().split()  # Lee los números de la prueba
                lista = [int(num) for num in numeros]
                listaAscendente = menor_mayor(lista)
                print(listaAscendente)
            except StopIteration:  # Cuando no hay más pruebas, termina el bucle
                break
main()
