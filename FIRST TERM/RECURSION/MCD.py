"""Dada una función recursiva para MCD cómo

MCD = M si N =0
MCD = MCD (N, M mod N) si N <> 0

Escriba un programa que le permita al usuario ingresar los valores para M y N desde la consola.
Una función recursiva es entonces llamada para calcular el MCD. El programa entonces imprime el valor para el MCD."""

import sys         #Librería

def mcd(M, N):                             #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if N == 0:                             #c1             N            c1             N
        return M                           #c2             1            c2             1
    else:
        return mcd(N, M % N)               #c3             1            c3             1
                                               # T(n)= O(N)               #T(n)= Ohm(N)
def main():
    for line in sys.stdin:
        try:
            M, N = map(int, line.strip().split())            #Los números para calcular MCD
        except ValueError:
            continue
        result = mcd(M, N)
        print("El Máximo Común Divisor (MCD) de", M, "y", N, "es", result)
main()

