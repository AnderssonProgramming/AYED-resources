import random


def busqueda_binaria(lista, start, end, goal):
    # Caso base
    if start > end:
        return False

    medio = (start + end) // 2

    if lista[medio] == goal:
        return True
    elif lista[medio] < goal:
        return busqueda_binaria(lista, medio + 1, end, goal)
    elif lista[medio] > goal:
        return busqueda_binaria(lista, start, medio - 1, goal)


list_size = int(input("¿Cuál es el tamaño de la lista? "))
goal = int(input("¿Cuál es el objetivo? "))

my_list = sorted([random.randint(0, 100) for i in range(list_size)])

find = busqueda_binaria(my_list, 0, len(my_list), goal)

print(my_list)
print(f'El elemento {goal} {"está" if find else "no está"} en la lista')
