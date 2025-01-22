from sys import stdin

contador = 0


def merge(s1, s2):
    global contador
    result = []
    s1_index, s2_index = 0, 0
    while s1_index < len(s1) and s2_index < len(s2):
        s1_element, s2_element = s1[s1_index], s2[s2_index]
        if s1_element <= s2_element:
            s1_index += 1
            result.append(s1_element)
        else:
            s2_index += 1
            result.append(s2_element)
            contador += len(s1) - s1_index
    if s1_index < len(s1):
        result += s1[s1_index:]
    if s2_index < len(s2):
        result += s2[s2_index:]
    return result


def merge_sort(s):
    size = len(s)
    if size <= 1:
        return s[:]
    half_1, half_2 = merge_sort(s[:(size // 2)]), merge_sort(s[(size // 2):])
    return merge(half_1, half_2)


def main():
    global contador
    Size = int(stdin.readline().strip())
    while Size != 0:
        lista = []
        for i in range(Size):
            element = int(stdin.readline().strip())
            lista.append(element)
        merge_sort(lista)
        print(contador)
        contador = 0
        Size = int(stdin.readline().strip())


main()
