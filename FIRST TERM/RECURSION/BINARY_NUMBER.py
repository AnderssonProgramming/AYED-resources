"Programe un método recursivo que transforme un número entero positivo a notación binaria."

import sys               #Librería

def a_binario(n):                                      #Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    if n == 0:                                         #c1             n           c1              n
        return '0'                                     #c2             1            c2             1
    elif n == 1:                                       #c3             n            c3             n
        return '1'                                     #c4             1            c4             1
    else:
        return a_binario(n // 2) + str(n % 2)          #c5             n            c5            n/2
                                                            # T(n)= O(n)               #T(n)= Ohm(n)
def main():
    for line in sys.stdin:
        try:
            n = int(line.strip())                                #Número para pasar a notación binaria
        except ValueError:
            continue
        resultado = a_binario(n)
        print("La representación binaria de", n, "es", resultado)

main()

