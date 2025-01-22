from sys import stdin


def main():
    casos = int(stdin.readline().strip())
    index = 0
    while index < casos:
        ordenN = int(stdin.readline().strip())
        secuencia = stdin.readline().strip().split()
        for n in range(ordenN):
            secuencia = [int(secuencia[s + 1]) - int(secuencia[s]) for s in range(len(secuencia) - 1)]
        print('Caso #{}:'.format(index + 1), ' '.join(map(str, secuencia)))
        index += 1

main()
