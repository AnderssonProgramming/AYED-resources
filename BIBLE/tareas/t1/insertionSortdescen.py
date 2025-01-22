from sys import stdin
from random import randint

LIMIT = 100
SIZE = 10

def insertionIndexBased( indexToSort, sequence):
    # IndexToSort > 0
    elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort-1]
    while elementToSort > beforeElement and indexToSort > 0:
        sequence[indexToSort], sequence[indexToSort-1] = sequence[indexToSort-1], sequence[indexToSort]
        indexToSort= indexToSort - 1
        elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort - 1]

def insertionSort( sequence ):
    for index in range(1, len(sequence)):
        insertionIndexBased(index, sequence)


def main():
    for i in range(randint(1,10)):
        sequence = [ randint(0,LIMIT) for x in range(SIZE)]
        print('Original: ', sequence)
        insertionSort(sequence)
        print('Ordenada: ',sequence)


main()