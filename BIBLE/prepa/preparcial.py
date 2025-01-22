from sys import stdin


def subcadena(cadena1, cadena2, i=0, j=0, total=[]):

    if cadena1[i] == cadena2[j]:
        total.append(cadena1[i])
    elif cadena1[i] != cadena2[j]:
        j+=1
    if j >= len(cadena2) - 1 and i >= len(cadena1) - 1:
        return total
    else:
        return subcadena(cadena1, cadena2, i+1)


def main():
    cadena1 = stdin.readline().strip().split()
    cadena2 = stdin.readline().strip().split()
    while cadena1 and cadena2:
        print(len(subcadena(cadena1, cadena2)))
        cadena1 = stdin.readline().strip().split()
        cadena2 = stdin.readline().strip().split()


main()
