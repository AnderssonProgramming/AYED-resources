from sys import stdin, stdout
def generar_campo(filas, columnas, campo):
    for i in range(filas):
        for j in range(columnas):
            if campo[i][j] == '*':
                continue
            count = 0
            for x in range(max(0, i - 1), min(filas, i + 2)):
                for y in range(max(0, j - 1), min(columnas, j + 2)):
                    if campo[x][y] == '*' and (x != i or y != j):
                        count += 1
            campo[i][j] = str(count)
    return campo
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