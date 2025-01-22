def leer_n():
    with open('entrada1.txt', 'r') as f:
        return [int(linea.strip()) for linea in f]

def generar_wonder_square(n):
    size = 2 * n - 1

    matriz = [[0 for i in range(size)] for j in range(size)]

    for i in range(n):
        for j in range(i, size - i):
            matriz[i][j] = matriz[j][i] = matriz[size - i - 1][j] = matriz[j][size - i - 1] = n - i

    return matriz

def imprimir_wonder_square(wonder_square):
    with open('salida1.txt', 'w') as f:
        for square in wonder_square:
            for row in square:
                f.write(" ".join(map(str, row)) + "\n")    #f.write escribe el contenido de la cadena al archivo, retornando la cantidad de caracteres escritos
            f.write("\n")

def main():
    print("Dado un número n, se deberá componer el WonderSquare de n, un WonderSquare de n se describe por la siguiente sucesión : ")
    ns = leer_n()
    wonder_squares = [generar_wonder_square(n) for n in ns]
    imprimir_wonder_square(wonder_squares)

main()
