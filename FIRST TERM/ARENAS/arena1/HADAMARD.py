import sys
def power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)  # forma eficiente
def hadamard(matrix, n):                                                             #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if n == 1:                                                                       #c1             1            c1             1
        return matrix[0][0]        #Caso base cuando tamaño matriz = 1               #c2             1            c2             1
    for i in range(n):                                                               #c3             n            c3             1
        for j in range(i + 1, n):                                                    #c4            n+1           c4             1
            if sum(matrix[i][k] != matrix[j][k] for k in range(n)) != n / 2:         #c5             n            c5             n
                return False                                                         #c6             1            c6             1
    return True                                                                      #c7             1            c7             1                                                                                    # T(n) = O(n)               T(n) = Ohm(n)
def check_hadamard(n, values):
    if not power_of_two(n):
        return "Imposible"        #Primer caso cuando la matriz Hadamard es imposible de hacer (depende: tam, elementos)
    matrix = crear_matriz(n)       #Cuando no es potencia de 2, el tamaño de la matriz
    for i in range(n):
        for j in range(n):
            matrix[i][j] = values[i * n + j] == 'T'
    return "Hadamard" if hadamard(matrix, n) else "No Hadamard" #Los otros dos casos cuando es potencia de 2
def crear_matriz(tam):
    matriz = [[False] * tam for _ in range(tam)]
    return matriz

for line in sys.stdin:
    n = int(line)
    values = next(sys.stdin).split()
    print(check_hadamard(n, values))




