# B. Escribir una función recursiva que devuelva la suma de un subarreglo de N enteros, límitado por indices (i,
# j)  en una lista de enteros L
from random import randint

SIZE = 10
SEED = 1e3


def sumSub(list, i, j):
    if i == j:
        return list[i]
    return list[i] + sumSub(list, i + 1, j)


def main():
    s1 = [359, 599, 79, 73, 924]
    print(sumSub(s1, 2, 4))
    """for i in range(100):
        s = [randint(1, SEED) for i in range(randint(5, SIZE))]
        print(sumSub(s, 1, 3)==sum(s[1:4]))"""


main()
