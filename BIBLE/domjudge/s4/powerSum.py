from sys import stdin


def powerSum(x, n, k=1):
    numN = (k ** n)
    if x == numN:
        return 1
    if x < numN:
        return 0
    return powerSum(x - numN, n, k + 1) + powerSum(x, n, k + 1)


def main():
    x = stdin.readline().strip()
    n = stdin.readline().strip()
    while x:
        x = int(x)
        n = int(n)
        print(powerSum(x, n))
        x = stdin.readline().strip()
        n = stdin.readline().strip()


main()