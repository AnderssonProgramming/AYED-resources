def sumRec(A, N):
    return 0 if N < 1 else A[N] + sumRec(A, N-1)

def main(A, N):
    return sumRec(A, N)


print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
