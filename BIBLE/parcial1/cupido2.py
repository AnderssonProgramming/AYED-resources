from sys import stdin
import math


def cupido(princ, size):
    mid = len(princ) // 2

    if len(princ) == 0:
        return -math.inf
    if princ[mid] >= size:
        return cupido(princ[:mid], size)
    return max(princ[mid], cupido(princ[mid + 1:], mid))

def main():
    cantPrinc, princ = int(stdin.readline().strip()), sorted(list(map(int, stdin.readline().strip().split())))
    cantSize, sizes = int(stdin.readline().strip()), list(map(int, stdin.readline().strip().split()))
    for size in sizes:
        print(cupido(princ, size) if cupido(princ, size) != -math.inf else 'X')

main()