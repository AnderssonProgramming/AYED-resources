from sys import stdin

def merge(A,B):
    indexLeft, indexRight, result = 0,0, []
    while indexLeft < len(A) and indexRight < len(B):
        elementLeft, elementRight = A[indexLeft], B[indexRight]
        result.append(min(elementRight, elementLeft))
        indexLeft = indexLeft + 1 if elementLeft < elementRight else indexLeft
        indexRight = indexRight + 1 if elementRight <= elementLeft else indexRight
    return result + (A[indexLeft:] if indexLeft < len(A) else B[indexRight:])

def mergeSort(A):
    if len(A) == 1:
        return A
    result = merge(mergeSort(A[:len(A)//2]), mergeSort(A[len(A)//2:]))
    return result

def main():
    lenght = int(stdin.readline().strip())
    while lenght != 0:
        lista = [int(stdin.readline().strip()) for index in range(lenght)]
        count = 0
        print(mergeSort(lista))
        lenght = int(stdin.readline().strip())

if __name__ == '__main__':
    main()