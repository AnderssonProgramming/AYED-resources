from sys import stdin


def sortElement(index, s, swaps):
    element, inter = s[index], index
    for k in range(index - 1, -1, -1):
        if element < s[k]:
            s[inter], s[k] = s[k], s[inter]
            element, inter = s[k], k
            swaps += 1
    return swaps


def insertionSort(s):
    swaps = 0
    for index in range(1, len(s)):
        swaps = sortElement(index, s, swaps)
    return swaps


def main():
    casos = int(stdin.readline().strip())
    for i in range(casos):
        enteroL = int(stdin.readline().strip())
        secuencia = list(map(int, stdin.readline().strip().split()))
        swaps = insertionSort(secuencia)
        print("Optimal train swapping takes {} swaps.".format(swaps))


main()
