def missing(n):
    count = 1
    resp = "nothing"
    for index in range(len(n)):
        if count != n[index]:
            resp = index - 1
        count += 1
    return resp


print(missing([1, 2, 3, 4, 6, 7, 8]))
