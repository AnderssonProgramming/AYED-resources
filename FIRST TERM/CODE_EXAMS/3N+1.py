from sys import stdin   #Biblioteca para leer entradas estándar

memo = {}

def numTNOne(n):           #Función que describe 3N+1 en general
    if n==1:
        return 1
    if n%2 == 0:
        return 1 + numTNOne(n // 2)
    return 1 + numTNOne(3 * n + 1)

def numTNOneP(n, M):       #Función que servirá de soporte para almacenar información y después guardarlo en la memoria
    if n==1:
        return 1
    if n%2 == 0:
        return 1 + numTNOneMemo(n // 2, M)
    return 1 + numTNOneMemo(3 * n + 1, M)
def numTNOneMemo(n, M):     #Función memoria
    if n in M.keys():
        return M[n]
    M[n] = numTNOneP(n, M)
    return M[n]

def map_numTNOneMemo(n):            #Función que recurrirá a guardar los datos en memo, que se creó como diccionario
    if n in memo.keys():
        return memo[n]
    memo[n] = numTNOneP(n, memo)
    return memo[n]

def maxNumTNOne(n,m):               #Retorna el máximo valor de hacer los cálculos del número n y m
     return max(map(map_numTNOneMemo, range(n,m+1)))


def main():
    line = stdin.readline().strip()     #Leer la línea y quita los espacios para poner la entrada estándar
    while line:
        n,m = map(int, line.split())    #Poner n,m en una sola línea separados por espacio
        print(n,m, maxNumTNOne(min(n,m), max(n,m)))
        line = stdin.readline().strip()         #Para que no quede en un bucle

main()