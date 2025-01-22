# Programe un método recursivo que transforme un número entero
# positivo a notación binaria.
def int_to_bin(n, bin=""):
    if n//2 == 0:
        return (bin+str(n % 2))[::-1]
    else:
        bin += str(n % 2)
        return int_to_bin(n//2, bin)


def main():
    for i in range(100):
        print("El binario de", i, "es", int_to_bin(i))


main()
