from sys import  stdin

def merge(A, B):
    indexRight, indexLeft, result = 0, 0, []
    while indexRight < len(A) and indexLeft < len(B):
        elementRight, elementLeft = A[indexRight], B[indexLeft]
        result.append(min(elementLeft, elementRight))
        indexRight = indexRight + 1 if elementRight < elementLeft else indexRight
        indexLeft = indexLeft + 1 if elementLeft <= elementRight else indexLeft
    return result + (A[indexRight:] if indexRight < len(A) else B[indexLeft:])


def mergeSort(A, count):
    if len(A) == 1:
        count += 1
        print(count)
        return A

    result = merge(mergeSort(A[:len(A)//2], count), mergeSort(A[len(A)//2:], count))
    return result


def main():
    lenght = int(stdin.readline().strip())
    while lenght != 0:
        lista = [int(stdin.readline().strip()) for index in range(lenght)]
        count = 0
        print(mergeSort(lista, count))
        lenght = int(stdin.readline().strip())

if __name__ == '__main__':
    main()

