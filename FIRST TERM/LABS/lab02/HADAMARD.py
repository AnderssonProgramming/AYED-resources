"""sys: Librería que interactúa con el intérprete de Python (archivo)"""
import sys

"""power_of_two: Función que define cuando un número es potencia de 2"""

def power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)  # forma eficiente

"""hadamard: Una manera de ver la función hadamard, con elementos de cada dos filas adyacentes a n/2 """

def hadamard(matrix, n):                                                             #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if n == 1:                                                                       #c1             1            c1             1
        return matrix[0][0]        #Caso base cuando tamaño matriz = 1               #c2             1            c2             1
    for i in range(n):                                                               #c3             n            c3             1
        for j in range(i + 1, n):                                                    #c4            n+1           c4             1
            if sum(matrix[i][k] != matrix[j][k] for k in range(n)) != n / 2:         #c5             n            c5             n
                return False                                                         #c6             1            c6             1
    return True                                                                      #c7             1            c7             1

                                                                                        # T(n) = O(n)               T(n) = Ohm(n)
"""check_hadamard: Función que depende de la anterior, para mostrar la característica de Hadamard"""

def check_hadamard(n, values):
    if not power_of_two(n):
        return "Imposible"        #Primer caso cuando la matriz Hadamard es imposible de hacer (depende: tam, elementos)
    matrix = crear_matriz(n)       #Cuando no es potencia de 2, el tamaño de la matriz
    for i in range(n):
        for j in range(n):
            matrix[i][j] = values[i * n + j] == 'T'
    return "Hadamard" if hadamard(matrix, n) else "No Hadamard" #Los otros dos casos cuando es potencia de 2

"""crear_matriz: Función que crea la matriz, empezando a llenando la matriz con valores booleanos (comodidad)"""

def crear_matriz(tam):
    matriz = [[False] * tam for _ in range(tam)]
    return matriz

"""stdin: dispositivo estándar de entrada para leer un archivo y hacer pruebas para que genere un archivo de salida"""
"""split: convertir cadenas de carácteres en una lista"""

for line in sys.stdin:
    n = int(line)
    values = next(sys.stdin).split()
    print(check_hadamard(n, values))




