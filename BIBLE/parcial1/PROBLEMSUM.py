from sys import stdin


def suma(s):
    suma = 0
    for i in range(len(s)):
        suma += int(s[i])
    return suma


def sumas(s, n):
    i = len(s)
    if len(s) == 0:
        return -1
    else:
        if suma(s[:i]) == n:
            return len(s)-1
        else:
            return sumas(s[:i-1], n)


def main():
    casos = int(stdin.readline().strip())
    for caso in range(casos):
        s, n = stdin.readline().strip().split()
        print(sumas(s, int(n)))
main()
