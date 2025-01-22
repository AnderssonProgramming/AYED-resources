from sys import stdin

def main():
    n = stdin.readline().strip().split(",")
    matriz = [[0 for i in range(int(n[1]))]for j in range(int(n[0]))]

    for i in range(int(n[0])):
        fila = stdin.readline().strip().split(",")
        for j in range(int(n[1])):
            matriz[i][j] = int(fila[j])
    n = stdin.readline().strip().split(",")
    matriz2 = [[0 for i in range(int(n[1]))]for j in range(int(n[0]))]
    for i in range(int(n[0])):
        fila = stdin.readline().strip().split(",")
        for j in range(int(n[1])):
            matriz2[i][j] = int(fila[j])
    matriz3 = [[0 for i in range(int(n[1]))] for j in range(int(n[0]))]
    for i in range(int(n[0])):
        for j in range(int(n[1])):
            for k in range(int(n[0])):
                matriz3[i][j] += matriz[i][k] * matriz2[k][j]

    for fila in matriz3:
        print(",".join(map(str,fila)))


main()