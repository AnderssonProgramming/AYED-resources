from sys import stdin

# Sequence debe implementar la funcion ord(e)
# Objeco debe implementar las funciones de comparacion enriquecidas
def insertionSortIndexBase(index, sequence):
    elementToSort, previousElement = sequence[index], sequence[index-1]
    # elementToSort > previousElement
    while elementToSort < previousElement and index > 0:
        sequence[index], sequence[index - 1], index = sequence[index -1], sequence[index], index -1
        elementToSort, previousElement = sequence[index], sequence[index - 1]


def insertionSort(sequence):
    for index in range(1, len(sequence)):
        insertionSortIndexBase(index, sequence)


def main():
    sequence = [int(x) for x in stdin.readline().split()]
    insertionSort(sequence)
    print(sequence)


if __name__ == '__name__':
    main()
