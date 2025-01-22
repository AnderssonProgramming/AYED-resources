"""ANDERSSON DAVID SÁNCHEZ MÉNDEZ"""

def busqueda_binaria(A, objetivo):
    if len(A) == 0:
        return "El número {} no se encuentra en el arreglo.".format(objetivo)
    elif len(A) == 1:
        return "El número {} se encuentra en el arreglo.".format(objetivo) if A[0] == objetivo else "El número {} no se encuentra en el arreglo.".format(objetivo)
    else:
        mid = len(A) // 2
        if A[mid] == objetivo:
            return "El número {} se encuentra en el arreglo.".format(objetivo)
        elif A[mid] > objetivo:
            return busqueda_binaria(A[:mid], objetivo)
        else:
            return busqueda_binaria(A[mid+1:], objetivo)

# Prueba
arreglo = [7, 23, 10, 56, 91, 12, 38, 16, 2, 5]
arregloF = arreglo.sort()  # Ordenamos el arreglo
print(busqueda_binaria(arreglo, 12))
print(busqueda_binaria(arreglo, 8))



