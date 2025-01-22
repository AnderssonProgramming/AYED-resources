from random import randint
from time import time

SIZE = 1e5
CASES = 2
LOWER = 0
HIGHER = 1e6

#Pre: A y B están ordenadas
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


def insertionSortElement(new_el, sequence):
    index = 0
    while index < len(sequence) and new_el > sequence[index]:
        index+=1
    return sequence[:index] + [new_el] + sequence[index:]


#pre: sequence is a list of comparable objects
def insertionSort(sequence):
    #print(sequence)
    for index in range(1,len(sequence)):
        elem = sequence[index]
        #print(elem, str(sequence[:index+1]) + '-->'+ str(insertionSortElement(elem, sequence[:index])), sequence[index+1:], insertionSortElement(elem, sequence[:index]) + sequence[index+1:])
        sequence = insertionSortElement(elem, sequence[:index]) + sequence[index+1:]


    return sequence


def main():
    for i in range(int(CASES)):
        A = [ randint(int(LOWER), int(HIGHER))  for j in range(int(SIZE))]
        #time0 = time()
        #sort_in = insertionSort(A)
        time1 = time()
        print("Insertion Sort time : {}".format(time1-time0))
        time0 = time()
        sort_in = mergeSort(A)
        time1 = time()
        print("Merge Sort time : {}".format(time1-time0))

main()