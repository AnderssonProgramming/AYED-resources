def sumPairs(ci, N):
    return 0 if ci > N else ci + sumPairs(ci+2, N)


def main(ci, N):
    return sumPairs(ci, N)


print(main(0, 14))
print(main(0, 5))
print(main(0, 30))
print(main(0, 17))