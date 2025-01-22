def MCD(M, N):
    N, M = min(M, N), max(M, N)
    print(M, N)
    return M if N == 0 else MCD(N, M % N)


def main(M, N):
    return 15, 6


print(main(15, 6))
print(main(24, 12))
print(main(3, 6))
print(main(100, 50))
