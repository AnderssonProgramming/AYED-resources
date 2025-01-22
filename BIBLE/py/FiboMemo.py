import math
import time

MEMO_SIZE = 1e3

M = [ None for i in range(int(MEMO_SIZE))] # Static Memory
M[0] = M[1] = 1

# M[n] -> O(1)
# M.insert(n) -> O[n]

M_DIM = {}
M_DIM[0] = M_DIM[1] = 1
# M_DIM[n] -> O(n lg(n))
# M_DIM[n] (Insert, put) -> O(n)


def fibo(n):
    #print('Contexto de =====', n)
    if n < 0:
        return -math.inf
    if n <= 1 :
        #print('El fibonacci de ', n, 'es', 1)
        return 1
    else:
        #print('Debo resolver =====', n-1 ,' ',  n-2)
        result = fibo(n-1) + fibo(n-2)
        #print('Resuelto contexto de ==== ', n, '===== :', 'El fibonacci de ', n, 'es', result)
        return result


def fiboMemo(n, M):
    #Aprox por Memoría estática
    #print('Pre:',n, M)
    if n in M.keys():
        return M[n]
    M[n] = fibo_p(n,M)
    #print('Pos:', n, M)
    return M[n]


def fibo_p(n, M):
    # print('Contexto de =====', n)
    if n < 0:
        return -math.inf
    if n <= 1:
        # print('El fibonacci de ', n, 'es', 1)
        return 1
    else:
        # print('Debo resolver =====', n-1 ,' ',  n-2)
        result = fiboMemo(n - 1, M) + fiboMemo(n - 2, M)
        # print('Resuelto contexto de ==== ', n, '===== :', 'El fibonacci de ', n, 'es', result)
        return result


def main():
    #print(M)
    n = 430
    print(M_DIM)
    time0 = time.time()
    print(fiboMemo(n,M_DIM))
    print(M_DIM)
    time1 = time.time()
    time2 = time.time()


main()



