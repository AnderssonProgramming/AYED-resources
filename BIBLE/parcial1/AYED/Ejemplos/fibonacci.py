from sys import stdin
import time


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)


def fiboMemo(n, M):
    if n <= 1 :
        return 1
    return memoFibo(n-1, M) + memoFibo(n-2, M)


def memoFibo(n, M):
    if M[n] is not None:
        return M[n]
    M[n] = fiboMemo(n, M)
    return M[n]


def memorizedFibonacci(n):
    M = [(None) if j > 1 else 1 for j in range(n+1)]
    return memoFibo(n, M)


def main():
    line = stdin.readline().strip()
    while line:
        n = int(line)
        ti = time.time()
        result = fibo(n)
        tf = time.time()
        print('Non Memorized fibonacci', result, (tf-ti))
        ti = time.time()
        result = memorizedFibonacci(n)
        tf = time.time()
        print('Memorized fibonacci', result, (tf-ti))
        line = stdin.readline().strip()

main()

