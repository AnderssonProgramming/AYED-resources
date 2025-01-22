def sort_recur(lista,i = 0,sort_list = []):
    """
    Funcion recursiva por pila, para ordenar una lista de forma ascendente.
    :param lista: lista para tener en cuenta al llenar la lista ordenada.
    :param i: indice que equivale al primer indice de la lista.
    :param sort_list: lista vacia que luego representara la lista ordenada.
    :return: Una lista ordenada.
    """
    if i == len(lista):#caso base de la recursion por pila
        return sort_list
    else:
        number = min(lista)#busco el minimo de la lista
        lista_2 = lista[:]#copia
        sort_list.append(number)#agregar el menor
        lista_2.remove(number)#elimino el menor
        return sort_recur(lista_2,i = 0,sort_list = sort_list[:])#llamado recursivo

#print(sort_recur([3,2,5,4,7]))


def suma(i,j,lista):
    """
    Recursion por pila para sumar los elementos de un subarreglo
    :param i: indice de inicio.
    :param j: indice de finalizacion
    :param lista: secuencia de elementos.
    :return: suma de los elementos del subarreglo.
    """
    if i == j:
        return lista[i]
    else:
        return lista[i] + suma(i+1,j,lista)


def conteo(n):
    """
    Recursion por cola, que retorna la suma desde un numero n hasta 2, sumando unicamente los pares.
    :param n: numero entero
    :return: suma de los numeros pares de n hasta 2
    """
    if n % 2 == 1:#condicion de si es par o impar
        n = n - 1#vuelvo un numero impar a par
    if n == 2:
        return 2
    else:
        return n + conteo(n - 2)#llamado recurrente


def MCD(M,N):
    """
    Funcion recurrente por cola para hallar el MCD entre dos numeros a traves del algoritmo de euclides.
    :param M: un numero entero
    :param N: un numero entero
    :return: el MCD entre dos numeros.
    """
    if N == 1:#MCD(
        return 1
    elif N == 0:
        return M
    else:
        return MCD(N,M % N)#


def int_to_binary(n,binary = ""):
    """
    Funcion recursiva por cola para convertir un numero positivo a binario
    :param n: numero positivo
    :param binary: parametro definido dentro de la funcion.
    :return: el numero binario.
    """
    if n//2 == 0:
        return binary + str(n%2)
    else:
        binary += str(n%2)
        return int_to_binary(n//2,binary)

def reves(s,index = 0):
    """
    Funcion
    :param s:
    :param index:
    :return:
    """
    if index < len(s) // 2:
        elemento = s[-index - 1]
        s[-index - 1] = s[index]
        s[index] = elemento
        index += 1
        reves(s, index)

    return s


                                                                #Peor caso.(len(s1)) = len((s2))
def merge(s1, s2):                                              # costo     #Tiempo
    result = []                                                     #c1         1
    s1_index, s2_index = 0,0                                        #c2         1
    while s1_index < len(s1) and s2_index < len(s2):                #c3         n
        s1_element, s2_element = s1[s1_index], s2[s2_index]         #c4         n - 1
        if s1_element <= s2_element:                                #c5         n - 1
            s1_index += 1                                           #c6         n - 1
            result.append(s1_element)                               #c7         n - 1
        else:                                                       #c8         n - 1
            s2_index += 1                                           #c9         n - 1
            result.append(s2_element)                               #c10        n - 1
    if s1_index < len(s1):                                          #c11        1
        result += s1[s1_index:]                                     #c12        1
    if s2_index < len(s2):                                          #c13        1
        result += s2[s2_index:]                                     #c14        1
    return result

                                                                    #total = O(n)


                                                                #mejor caso.(len(s1)) = len((s2)) = 1
def merge(s1, s2):                                              # costo     #Tiempo
    result = []                                                     #c1         1
    s1_index, s2_index = 0,0                                        #c2         1
    while s1_index < len(s1) and s2_index < len(s2):                #c3         2
        s1_element, s2_element = s1[s1_index], s2[s2_index]         #c4         1
        if s1_element <= s2_element:                                #c5         1
            s1_index += 1                                           #c6         1
            result.append(s1_element)                               #c7         1
        else:                                                       #c8         1
            s2_index += 1                                           #c9         1
            result.append(s2_element)                               #c10        1
    if s1_index < len(s1):                                          #c11        1
        result += s1[s1_index:]                                     #c12        1
    if s2_index < len(s2):                                          #c13        1
        result += s2[s2_index:]                                     #c14        1
    return result

                                                                    #total = O(1) constante.







