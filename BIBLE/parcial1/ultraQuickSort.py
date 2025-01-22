# Nombre: Juan Camilo Bazurto Arias
# Carné: 2167888
# Documento: 1000521079

from sys import stdin

contador = 0


def merge(s1, s2):  # --> O(n) why ?
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

    # Remaining elements on left-side
    if s1_index < len(s1):
        result += s1[s1_index:]
    # Remaining elements on right-side
    if s2_index < len(s2):
        result += s2[s2_index:]
    return result


def merge_sort(s):
    # 0 -  La secuencia es divisible ?
    size = len(s)
    if size <= 1:
        return s[:]  # --> subsequence from 0 --> len(s)
    # 1 -  Dividir la secuencia en mitades
    # 2 -  Ordenar Las mitades ( n//2 )
    half_1, half_2 = merge_sort(s[:(size // 2)]), merge_sort(s[(size // 2):])
    # 3 -  Mezclar las mitades
    return merge(half_1, half_2)


def main():
    global contador
    elements = stdin.readline().strip()
    while elements:
        elements = int(elements)
        secuencia = []
        for i in range(elements):
            elem = stdin.readline().strip()
            secuencia.append(elem)
        merge_sort(secuencia)
        print(contador)
        contador = 0
        elements = stdin.readline().strip()

main()