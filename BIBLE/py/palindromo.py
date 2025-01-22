def main():
    cadena = input('Ingrese su cadena --> ')
    cadena = list(cadena)
    cadena2 = [cadena[i] for i in range(len(cadena)-1, -1, -1)]
    if cadena2 == cadena:
        print(True)
    else:
        print(False)
main()