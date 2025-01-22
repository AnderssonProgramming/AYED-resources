def inverseRec(A):
    if len(A) == 1:
        return A
    i = A[len(A)-1]
    A.remove(i)
    return [i] + inverseRec(A)


def main(A):
    return inverseRec(A)


print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(main([2, 4, 6, 8, 10, 12, 14, 16]))
print(main([1, 3, 5, 7, 9, 11, 13, 15, 17]))
print(main([2, 1, 4, 3, 6, 5, 8, 7]))
