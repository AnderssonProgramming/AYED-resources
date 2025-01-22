from sys import stdin


def insertionSortIndexBase(index, sequence):
    count = 0
    elementToSort, previousElement = sequence[index], sequence[index-1]
    while elementToSort < previousElement and index > 0:
        sequence[index], sequence[index - 1], index = sequence[index -1], sequence[index], index -1
        elementToSort, previousElement = sequence[index], sequence[index - 1]
        count += 1
    return count

def insertionSort(sequence):
    m = 0
    for index in range(1, len(sequence)):
        count = insertionSortIndexBase(index, sequence)
        m = count + m
    return m

def main():
    casos = int(stdin.readline().strip())
    wagons = stdin.readline().strip()
    while wagons:
        sequence = [int(x) for x in stdin.readline().split()]
        count = insertionSort(sequence)
        print("Optimal train swapping takes", count, "swaps.")
        wagons = stdin.readline().strip()



if __name__ == '__name__':
    main()


main()