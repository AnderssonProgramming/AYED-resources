from sys import stdin
def merge(A=[], B=[]):
    i,j, result = 0,0, []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1
    # Alguna de las secuencias tiene restante
    if i < len(A):
        result += A[i:]
    else:
        result += B[j:]
    return result
# pre : A es una secuencia de elementos comparables
# pos : Los elementos estan ordenados
def mergeSort(A=[]):
    if len(A) <= 1:
        return A
    half = len(A)//2
    #Dividir
    #print('Dividir A={}, left={}, right={}'.format(A, A[:half], A[half:]))
    left, right = mergeSort(A[:half]), mergeSort(A[half:])
    #print('Conquistar A={}, sorted_left={}, sorted_right={}'.format(A, left, right))
    #Conquistar
    result = merge(left, right) #Combinar
    #print('Combinar A={}, result = {}'.format(A, result))
    return result

def findMissingNumber(lista, N):
    total = N * (N + 1) // 2
    sum_of_elements = sum(lista)
    return total - sum_of_elements
def main():
    line = stdin.readline().strip()
    while line:
        lista = list(map(int,line.split()))
        print(mergeSort(lista))
        N = max(lista)  # Assuming that max element is equal to N
        missNumber = findMissingNumber(lista, N)
        print("missing",missNumber)
        line = stdin.readline().strip()
main()