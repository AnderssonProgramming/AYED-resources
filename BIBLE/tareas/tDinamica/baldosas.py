memoria = {"0": "1", "1": "0"}


def baldosas(n):
    if n == 1:
        return 0
    elif n == 0:
        return 1
    return baldosas(n - 2) + baldosas(n - 1)


def baldosaS(n, memoria):
    if n == 1:
        return memoria["1"]
    elif n == 0:
        return memoria["0"]
    else:
        return memoria(n - 2, memoria) + memoria(n - 1, memoria)


def memoria(n, memoria):
    if n in memoria.keys():
        return memoria[n]
    memoria[n] = baldosaS(n, memoria)
    return memoria[n]
