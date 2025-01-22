from sys import stdin


def functionNp(num, i=1):
    if num == 1:
        return i
    else:
        if num % 2 == 0:
            return functionNp(num // 2, i + 1)
        else:
            return functionNp(num * 3 + 1, i + 1)


def maximCycle(i, j, mayor=0):
    i, j = min(i, j), max(i, j)
    if i == j:
        return mayor
    else:
        if functionNp(i) > mayor:
            return maximCycle(i + 1, j, functionNp(i))
        else:
            return maximCycle(i + 1, j, mayor)


def main():
    index = stdin.readline().strip().split()
    while index:
        print(index[0], index[1], maximCycle(int(index[0]), int(index[1])))
        index = stdin.readline().strip().split()


main()