"""D. Dada una función recursiva para MCD cómo ​ MCD = M si N =0 MCD = MCD (N, M mod N) si N <> 0 ​ Escriba un
programa que le permita al usuario ingresar los valores para M y N desde la consola. Una función recursiva es
entonces llamada para calcular el MCD. El programa entonces imprime el valor para el MCD. """
from sys import stdin


def MCD(m, n):
    if n == 0:
        return m
    else:
        return MCD(n, m % n)


def main():
    nums = stdin.readline().strip().split()
    print(MCD(int(nums[0]), int(nums[1])))
    print('---------------')
    print("MCD de", 450,"y", 360)
    print("es:", MCD(450, 360))


main()
