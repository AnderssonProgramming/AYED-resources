def lessElement(a):
    index = 0
    if len(a) == 1:
        return a[index]
    else:
        if a[index] < a[index + 1]:
            a[index], a[index + 1] = a[index + 1], a[index]
        return lessElement(a[index + 1:])


def missingElement(a, i=0):
    if not a:
        return 1
    if i + 1 == a[i]:
        return missingElement(a, i + 1)
    else:
        return i + 1


def merge(s1, s2):  # --> O(n) why ?
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
    result = merge(half_1, half_2)
    return ''.join(result)


def mult(num, i, num2, j=1):
    if j == i:
        return num
    else:
         return mult(num * num2, i, num2, j + 1)

def exponent(num, e):
    if e == 0:
        return 1
    elif e == 1:
        return num
    else:
        halfl, halfr = mult(num, e//2, num), mult(num, (e+1)//2, num)
        return halfl * halfr


"""N1 = [2, 1, 2, 3, 4]
print(N1, 'min:', lessElement(N1))
N2 = [8, 5, 4, 34, 10, 3]
print(N2, 'min:', lessElement(N2))"""

"""N1 = [1, 2, 3, 4, 6, 7, 8]
N2 = [1, 2, 3, 4, 5, 6, 8, 9]
print(N1, 'missing:', missingElement(N1))
print(N2, 'missing:', missingElement(N2))"""

# print(merge_sort('ALGORITMO'))
print('4 elevado a la 6:', exponent(4, 6))
print('2 elevado a la 3:', exponent(2, 3))
print('5 elevado a la 4:',exponent(5, 4))
