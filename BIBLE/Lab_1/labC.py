"""C. Escribir una función y un programa que encuentre la suma de los enteros positivos pares desde N hasta 2."""


def sumPares(n):

    if n == 2:
        return 2
    else:
        if n % 2 == 0:
            return n + sumPares(n - 2)
        else:
            return n - 1 + (sumPares(n - 3) if n - 3 >= 2 else 0)

def main():
    for i in range(2, 22):
        print("n =", i, "Resultado es:", sumPares(i))

main()

