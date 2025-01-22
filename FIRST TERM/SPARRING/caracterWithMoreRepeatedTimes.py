def leer_entradas():
    with open('entrada.txt', 'r') as f:
        return [linea.strip() for linea in f]

def resolución_problema(S):
    caracterMáximo = ""
    maxCont = 0
    caracteresConMaxCont = []

    for i in S:
        contarCaracteres = S.lower().count(i.lower())

        if contarCaracteres > maxCont:
            caracterMáximo = i
            maxCont = contarCaracteres
            caracteresConMaxCont = [i]  # Reinicia la lista con el nuevo máximo

        elif contarCaracteres == maxCont and i.lower() not in caracteresConMaxCont:
            caracteresConMaxCont.append(i)  # Agrega el carácter a la lista si tiene el mismo número de repeticiones

    return caracteresConMaxCont, maxCont, caracterMáximo

def mostrar_resultados(resultados):
    with open('salida.txt', 'w') as f:
        for entrada, (caracteresConMaxCont, maxCont, caracterMáximo) in resultados.items():
            if len(caracteresConMaxCont) > 1:
                f.write(f"Para la entrada '{entrada}':\nHay dos o más caracteres con igual cantidad máxima de repeticiones: {caracteresConMaxCont} con {maxCont} veces\n\n")
            else:
                f.write(f"Para la entrada '{entrada}':\nEl carácter que más se repite es: {caracterMáximo}\nCon un número de repeticiones de: {maxCont}\n\n")

def main():
    print("Dada una cadena S, compuesta por caracteres: c0, c1, c2 ...... cn")
    print("Determinar aquel caracter ci el cual tiene el mayor número de repeticiones (No necesariamente contiguas) dentro de S:")
    entradas = leer_entradas()
    resultados = {}

    for entrada in entradas:
        caracteresConMaxCont, maxCont, caracterMáximo = resolución_problema(entrada)
        resultados[entrada] = (caracteresConMaxCont, maxCont, caracterMáximo)

    mostrar_resultados(resultados)


main()

