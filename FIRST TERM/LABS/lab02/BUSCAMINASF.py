from sys import stdin, stdout


def generar_campo(filas, columnas, campo):                                  # Cost (O)    #Times (O)  #Cost (Ohm)    #Times (Ohm)
    for i in range(filas):                                                  #   c1            n           c1              n
        for j in range(columnas):                                           #   c2            n           c2              n
            if campo[i][j] == '*':                                          #   c3           n^2          c3              1
                continue                                                    #   c4            1           c4              0
            count = 0                                                       #   c5            1           c5              1
            for x in range(max(0, i - 1), min(filas, i + 2)):               #   c6           n+1          c6              1
                for y in range(max(0, j - 1), min(columnas, j + 2)):        #   c7           n+1          c7              1
                    if campo[x][y] == '*' and (x != i or y != j):           #   c8            n           c8              1
                        count += 1                                          #   c9            n           c9              1
            campo[i][j] = str(count)                                        #   c10           n           c10             1
    return campo                                                            #   c11           1           c11             1
                                                                            # T(n) = O(n^2)                  T(n) = Ohm(n)

def imprimir_campo(campo):
    for fila in campo:
        print("".join(fila))


# Leer la entrada y procesar los campos de minas
case_number = 1
while True:
    entrada = stdin.readline().strip()
    if entrada == "0 0":
        break

    try:
        n, m = map(int, entrada.split())
        campo = [list(stdin.readline().strip()) for _ in range(n)]

        # Generar el campo de minas
        campo = generar_campo(n, m, campo)

        # Imprimir el resultado solo si no es un campo vacío
        if campo:
            stdout.write(f"Field #{case_number}:\n")
            imprimir_campo(campo)
            case_number += 1
            stdout.write("\n")

    except ValueError:
        # Si la entrada no tiene el formato esperado, ignorarla
        continue