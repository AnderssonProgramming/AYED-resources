# Juan Camilo Rojas Castro
# AYED Problemas de Calentamiento
# 06/08/2020

# Punto 1

def caracter(cadena):
    """Encuentra el caracter mas repetido en una cadena de caracteres"""
    palabra = (list(cadena))
    mayor = 0
    letra = "z"
    for i in range(len(palabra)):
        indice = palabra[i]
        contador = 0
        for j in range(len(palabra)):
            if palabra[j] == indice:
                contador = contador + 1
            if contador > mayor:
                mayor = contador
                letra = palabra[j]

    print(str(letra)+"->"+str(mayor))

# caracter("a1a1a1a")

# Punto 2

def wondersqr(numero):
    """A partir de un numero dado se compone un wondersquare"""
    if numero > 1:
        matriz = [[0 for i in range(2 * numero - 1)] for j in range(2 * numero - 1)]
        matriz[(numero//2)+1][(numero//2)+1] = 1
    else:
        matriz = [1]

    # Parte Superior e Inferior
    matriz[0] = [numero for i in range(len(matriz))]
    matriz[-1] = [numero for i in range(len(matriz))]
    # Lados
    for i in range(len(matriz)):
        matriz[i][0] = numero
        matriz[i][-1] = numero
    # Centro
    k = numero
    r = 1
    b = 2
    while k > 1:
        for i in range(r, len(matriz)-r):
            matriz[i][r] = numero - r
            matriz[r][i] = numero - r
            matriz[-b][i] = numero - r
            matriz[i][-b] = numero - r
        k = k - 1
        r = r + 1
        b = b + 1
    # Impresion
    for row in matriz:
        print(' '.join(map(str, row)))


# wondersqr(6) 'Prueba'

# Punto 3

def palindromo(palabra):
    """A partir de una cadena determina si es un palindromo"""
    if palabra == palabra[::-1]:
        print(True)
    else: print(False)

#palindromo("anitalavalatina") 'Prueba'

# Punto 4

def MCD(i, j):
    """Dado dos numeros encuentra su MCD"""
    mayor = 0
    k = True
    if i > j:
        c = j
    else: c = i
    while k==True:
        if i%c == 0 and j%c == 0:
            k = False
            mayor = c
        c = c - 1
    print(mayor)
#MCD(12, 6) 'Prueba'
