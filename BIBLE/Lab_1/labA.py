# A. Escriba una función recursiva que ordene de menor a mayor una lista de enteros basándose en la siguiente idea:
# coloque el elemento más pequeño en la primera ubicación, y luego ordene el resto del arreglo con una llamada
# recursiva.
from random import randint

SIZE = 10
SEED = 1e3


def minM(s, index):                                               #Cost         #Time
    if index == len(s):                                           # C1          n + 1
        return s                                                  # C2          1
    else:                                                         # C3          n
        minNum = min(s[index:])                                   # C4          n
        if minNum != s[index]:                                    # C5          n
            pos = s.index(minNum)                                 # C6          n - 1
            s[index], s[pos] = s[pos], s[index]                   # C7          n - 1

            return minM(s, index + 1)                             # C8          n - 1
        else:                                                     # C9          1

            return minM(s, index + 1)                             # C10         1

                                                                  # Toral = C1 + C2 + n(C1 + C3 + C4 + C5 + C6 + C7 + C8) + C9 + C10 - C6 - C7 - C8
                                                                  # O(n): lineal

def main():
    s1 = [80, 717, 384, 597, 277, 24, 245, 46]
    print(minM(s1, 0))

    #s = [randint(1, SEED) for i in range(randint(1, SIZE))]
    #print(minM(s, 0))


main()
