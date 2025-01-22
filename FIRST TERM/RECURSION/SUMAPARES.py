"""Escribir una función y un programa que encuentre la suma de los enteros positivos pares desde N hasta 2."""

import sys                #Librería

def sumaPares(n):                            #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if n < 2:                                #c1             n            c1             n
        return 0                             #c2             1            c2             1
    elif n % 2 != 0:                         #c3             n            c3             n
        return sumaPares(n-1)                #c4            n-1           c4             n-1
    else:
        return n + sumaPares(n-2)            #c5             1           c5              1
                                                  #T(n)= O(n)               #T(n)= Ohm(n)
def main():
    for line in sys.stdin:
        try:
            n = int(line.strip())                       #Número a tener en cuenta
        except ValueError:
            continue
        sumaParesF = sumaPares(n)
        print("La suma de los pares desde",n,"hasta 2 es de",sumaParesF)

main()

