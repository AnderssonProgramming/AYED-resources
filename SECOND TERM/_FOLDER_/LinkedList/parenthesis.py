"""Desarrolle un algoritmo que identifique si una cadena de texto contiene una lista de paréntesis
correctamente anidados y balanceados, por ejemplo:"""
# Importa la biblioteca requerida
from sys import stdin

def check_parentheses(s):
    # Define los pares de paréntesis
    combinaciones= {'(': ')', '[': ']', '{': '}'}

    # Inicializa una pila para llevar un registro de los paréntesis de apertura
    stack = []

    # Itera sobre los caracteres en la cadena
    for i, char in enumerate(s):
        # Si el carácter es un paréntesis de apertura, lo agrega a la pila
        if char in combinaciones:
            stack.append(char)
        # Si el carácter es un paréntesis de cierre
        elif char in combinaciones.values():
            # Si la pila está vacía o el elemento en la cima de la pila no coincide con el paréntesis de cierre
            if not stack or combinaciones[stack[-1]] != char:
                # Imprime "Incorrecto" y la posición del paréntesis mal ubicado
                print("Incorrecto, el primer paréntesis mal ubicado está en la posición",i,)
                return ""
            # Si el elemento en la cima de la pila coincide con el paréntesis de cierre, saca el elemento de la pila
            else:
                stack.pop()

    # Si la pila no está vacía después de iterar sobre la cadena, imprime "Incorrecto" y la posición del primer paréntesis de apertura que no se cerró
    if stack:
        print("Incorrecto, el primer paréntesis mal ubicado está en la posición", s.index(stack[0]))
        return ""
    else:
        # Si la pila está vacía, imprime "Correcto"
        print("Correcto")
    return ""

# Lee múltiples líneas desde la consola
for line in stdin:
    # Elimina el carácter de nueva línea al final de la línea
    line = line.rstrip('\n')
    # Verifica los paréntesis en la línea
    check_parentheses(line)

