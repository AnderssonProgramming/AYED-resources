from sys import stdin


def outSecuencia(i, secuencia):
    print('Caso #{}:'.format(i+1), ' '.join(map(str, secuencia)))


def main():
    casos = int(stdin.readline().strip())
    index = 0
    while index < casos:
        ordenN = int(stdin.readline().strip())
        secuencia = stdin.readline().strip().split()
        for n in range(ordenN):
            secuencia = [int(secuencia[s+1]) - int(secuencia[s]) for s in range(len(secuencia)-1)]
        outSecuencia(index, secuencia)
        index += 1
main()