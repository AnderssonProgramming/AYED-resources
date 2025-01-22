"""PROGRAMA <Prueba de calentamiento>

================================================================

ASIGNATURA : AYED
OBJETIVO : Hacer diferentes programas propuestos
AUTOR(ES) : Andersson David Sánchez Méndez
FECHA: 01/02/2024
"""

#PRIMER PROGRAMA
def pedir_cadena():

    S = input("Digite cadena de carácteres a tener en cuenta: ")

    return S

def resolución_problema(S):

    caracterMáximo = ""
    maxCont = 0
    caracteresConMaxCont = []

    for i in S:
        contarCaracteres = S.lower().count(i.lower())

        if contarCaracteres > maxCont:
            caracterMáximo = i
            maxCont = contarCaracteres
            caracteresConMaxCont = [i]  # Reinicia la lista con el nuevo máximo

        elif contarCaracteres == maxCont and i.lower() not in caracteresConMaxCont:
            caracteresConMaxCont.append(i)  # Agrega el carácter a la lista si tiene el mismo número de repeticiones

    return caracteresConMaxCont, maxCont, caracterMáximo

def main():
    print("Dada una cadena S, compuesta por caracteres: c0, c1, c2 ...... cn")
    print("Determinar aquel caracter ci el cual tiene el mayor número de repeticiones (No necesariamente contiguas) dentro de S:")

    S = pedir_cadena()

    caracteresConMaxCont, maxCont, caracterMáximo = resolución_problema(S)

    if len(caracteresConMaxCont) > 1:
        print("Hay dos o más caracteres con igual cantidad máxima de repeticiones:", caracteresConMaxCont, "con", maxCont, "veces")

    else:
        print("El carácter que más se repite es:", caracterMáximo)
        print("Con un número de repeticiones de:", maxCont)

main()


#SEGUNDO PROGRAMA
def pedir_n():
    n = -1

    while n <= 0:
        n = int(input("Ingrese el número n: "))

    return n


def generate_wonder_square(n):
    size = 2 * n - 1

    matriz = [[0 for i in range(size)] for j in range(size)]

    for i in range(n):
        for j in range(i, size - i):
            matriz[i][j] = matriz[j][i] = matriz[size - i - 1][j] = matriz[j][size - i - 1] = n - i

    return matriz


def print_wonder_square(wonder_square):
    for row in wonder_square:
        print(" ".join(map(str, row)))


def main():
    print("Dado un número n, se deberá componer el WonderSquare de n, un WonderSquare de n se describe por la siguiente sucesión : ")
    n = pedir_n()
    wonder_square = generate_wonder_square(n)
    print_wonder_square(wonder_square)

main()


#TERCER PROGRAMA

from unidecode import unidecode

def pedir_datos():
    S = input("Digite cadena de carácteres a tener en cuenta: ")
    return "".join(unidecode(S.lower()).split())

def determinarPalíndromo(palabra):
    palabra = "".join(unidecode(palabra.lower()).split())
    return palabra == palabra[::-1]

def main():
    print("Determinar si una cadena S es un palíndromo, un palíndromo es aquella sucesión de caracteres en donde ci = cn-i para todo i > 0 : ")

    S = pedir_datos()

    print(S == S[::-1] )

main()



#CUARTO PROGRAMA

def pedir_datos():
    i=-1
    j=-1

    while i < 0 and j < 0 :
        i=int(input("Ingrese un número entero: "))
        j=int(input("Ingrese otro número entero: "))
    
    return [i,j]
        
def maximo_comun_divisor(i, j):

    if j == 0:
        return i
    else:
        print("maximo_comun_divisor(",j ,",", i%j,")")
  
        return maximo_comun_divisor(j , i%j)

def imprimir_datos(i,j,MCD):
    print("El máximo común divisor de ",i,"y",j,"es: ",MCD)

def main():
    print("Determinar el MCD de dos números enteros i,j : ")
    [i,j]=pedir_datos()
    MCD=maximo_comun_divisor(i, j)
    imprimir_datos(i,j,MCD)

main()    

