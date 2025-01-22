from sys import stdin

def main():
    cadena = stdin.readline().strip()
    while cadena:
        letraM = ''
        numM = 0
        for letra in cadena:
            numC = cadena.count(letra)
            if numC > numM:
                letraM = letra
                numM = numC
        print(letraM, '->', numM)
        cadena = stdin.readline().strip()
main()