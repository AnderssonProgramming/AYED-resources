from random import randint
import time

SIZE = 1e7
SEED = 20
TESTS = 10

def lineal_search(A, e):
    index, found = 0, False
    while index < len(A) and not found:
        found = A[index] == e
        index += 1
    return found

def binSearch(A, e):
    n = len(A)
    # Casos Base
    if len(A) == 0:
        return False
    if len(A) == 1:
        return A[0] == e
    if A[n//2] == e:
        return True
    # Casos Inductivos
    if A[n//2] > e:
        return binSearch(A[:(n // 2)], e)
    elif A[n//2] < e:
        return binSearch(A[(n//2):], e)


def main():
    for test in range(TESTS):
        seq = sorted([ randint(0, SEED) for x in range(int(SIZE))])
        search_e = randint(0, SEED)
        time_0 = time.time()
        binSearch(seq, search_e)
        time_1 = time.time()
        time_2 = time.time()
        lineal_search(seq, search_e)
        time_3 = time.time()
        #print(seq, search_e, search_e in seq)
        print('Binary:',time_1-time_0, ' Lineal Search', time_3-time_2 )

main()

