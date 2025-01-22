from sys import stdin


def trib(n, back, cont):
    if n <= 1:
        return 0, cont
    elif n == 1:
        return 1, cont
    acum = 0
    for i in range(1, back + 1):
        cont += 1
        ans, cont = trib(n - i, back, cont)
        acum = acum + ans
    return acum, cont


def main():
    n, back = map(int, stdin.readline().strip().split())
    i = 1
    while n <= 61 and back <= 60:
        cont = 1
        ans, cont = trib(n, back, cont)
        print("Case {}:".format(i), cont)
        i += 1
        n, back = map(int, stdin.readline().strip().split())


main()

"""
3 3
4 4
5 5
6 6
7 7
8 8
9 9
61 61
"""
