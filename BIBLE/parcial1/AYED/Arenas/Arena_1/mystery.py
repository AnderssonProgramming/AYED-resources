def function_mystery(n):
    r = 0
    cont_i = 0
    cont_j = 0
    cont_k = 0
    for i in range(1, n - 1):
        cont_i += 1
        for j in range(i + 1, n):
            cont_j += 1
            for k in range(1, j):
                cont_k += 1
                r = r + 1
    return r


print(function_mystery(10))


