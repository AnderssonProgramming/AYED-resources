
from sys import stdin

def check_parentheses(s):
    # Define los pares de paréntesis
    combinaciones= {'(': ')', '[': ']'}

    # Inicializa una pila para llevar un registro de los paréntesis de apertura
    stack = []

    # Itera sobre los caracteres en la cadena
    for char in s:
        # Si el carácter es un paréntesis de apertura, lo agrega a la pila
        if char in combinaciones:
            stack.append(char)
        # Si el carácter es un paréntesis de cierre
        elif char in combinaciones.values():
            # Si la pila está vacía o el elemento en la cima de la pila no coincide con el paréntesis de cierre
            if not stack or combinaciones[stack[-1]] != char:
                # Retorna "No"
                return "No"
            # Si el elemento en la cima de la pila coincide con el paréntesis de cierre, saca el elemento de la pila
            else:
                stack.pop()

    # Si la pila no está vacía después de iterar sobre la cadena, retorna "No"
    if stack:
        return "No"
    else:
        # Si la pila está vacía, retorna "Yes"
        return "Yes"

# Lee múltiples líneas desde la consola
n = int(stdin.readline())
for i in range(n):
    s = stdin.readline().strip()
    # Verifica los paréntesis en la línea
    print(check_parentheses(s))
