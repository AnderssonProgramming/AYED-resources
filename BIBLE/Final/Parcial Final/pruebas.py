I = iter([23, 10, 7, 18])
Y = [next(I) * i for i in range(sum(1 for _ in I))]
assert tuple(Y) == (0, 10, 14, 54)
