"Programe un método recursivo que invierta los números de un arreglo de enteros"

import sys                #Librería

def lista():
    lista = []
    n = int(sys.stdin.readline().strip())                           #lista tiene cantidad y los números del arreglo
    numeros = sys.stdin.readline().strip().split()

    for i in range(n):
        try:
            numero = int(numeros[i])
        except ValueError:
            continue

        lista.append(numero)

    return lista

def reverse_Array(list):                                     #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if len(list) == 0:                                       #c1             n            c1             n
        return []                                            #c2             1            c2             1
    else:
        return [list[-1]] + reverse_Array(list[:-1])         #c3             n-1          c3             n-1
                                                               # T(n)= O(n)               #T(n)= Ohm(n)

def main():
    with open('entrada6.txt', 'r') as f:  # Abre el archivo 'entradas.txt' en modo lectura
        while True:
            try:
                line = next(f).strip()  # Lee la siguiente línea y elimina los espacios en blanco
                if not line:  # Si la línea está vacía, pasa a la siguiente línea
                    continue
                n = int(line)  # Convierte la línea en un número entero
                numeros = next(f).strip().split()  # Lee los números de la prueba
                lista = [int(num) for num in numeros]
                ArregloInvertido = reverse_Array(lista)
                print("Arreglo invertido: ", ArregloInvertido)
            except StopIteration:  # Cuando no hay más pruebas, termina el bucle
                break

main()

